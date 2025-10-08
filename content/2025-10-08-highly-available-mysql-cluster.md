---
title: "How Flipkart Built a Highly Available MySQL Cluster for 150+ Million Users"
date: 2025-10-08
type: diagram
tags:
  - mysql
  - high-availability
  - cluster
---

### High-Availability Model

```mermaid
graph TD
    subgraph "Clients"
        App1
        App2
        App3
    end

    subgraph "MySQL Cluster"
        Primary[("Primary DB")]
        Replica1[("Replica DB 1")]
        Replica2[("Replica DB 2")]
    end

    App1 -- Writes --> Primary
    App2 -- Writes --> Primary
    App3 -- Writes --> Primary

    Primary -- "Asynchronous Replication" --> Replica1
    Primary -- "Asynchronous Replication" --> Replica2

    App1 -- Reads --> Replica1
    App2 -- Reads --> Primary
    App3 -- Reads --> Replica2
```

### Failure Detection Architecture

```mermaid
graph TD
    subgraph "Database Nodes"
        Agent1[Agent] --> DB1("MySQL Primary")
        Agent2[Agent] --> DB2("MySQL Replica")
    end

    subgraph "Monitoring System"
        Monitor1[Monitor]
        Monitor2[Monitor]
        Orchestrator
        
        Monitor1 <--> Monitor2
    end

    subgraph "ZooKeeper"
        ZK
    end

    Agent1 -- "Health Report (10s)" --> Monitor1
    Agent2 -- "Health Report (10s)" --> Monitor2

    Monitor1 -- "Writes Status (10s)" --> ZK
    Monitor2 -- "Writes Status (10s)" --> ZK

    Monitor1 -- "Suspects Failure" --> Orchestrator
    Monitor2 -- "Suspects Failure" --> Orchestrator

    Orchestrator -- "Verifies Failure & Initiates F..." --> MySQL_Cluster(("MySQL Cluster"))
```

### Failover Workflow

```mermaid
sequenceDiagram
    participant Agent
    participant Monitor
    participant Orchestrator
    participant OldPrimary as Old Primary
    participant Replica
    participant DNS

    Agent->>Monitor: Health Report
    Monitor->>Orchestrator: Suspect Failure
    Orchestrator->>OldPrimary: Verify Failure
    Orchestrator->>Replica: Verify Connectivity
    alt Failure Confirmed
        Orchestrator->>Orchestrator: Stop Monitoring
        Orchestrator->>Replica: Allow Relay Log Catch-up
        Orchestrator->>OldPrimary: Set to Read-Only (if reachable)
        Orchestrator->>OldPrimary: Stop Old Primary (if possible)
        Orchestrator->>Replica: Promote to Primary
        Orchestrator->>DNS: Update DNS Record
    end
```

### Split-Brain Scenario

```mermaid
graph TD
    subgraph "Clients"
        Client1
        Client2
    end

    subgraph "Data Center 1"
        Primary
    end

    subgraph "Data Center 2"
        Replica
        Orchestrator
    end
    
    subgraph "Network Partition"
        P((X))
    end

    %% Solid Links
    Client1 --> Primary
    Client2 --> Primary
    Primary -- "Replication" --> Replica
    Orchestrator -- "Monitors" --> Primary
    Orchestrator -- "Monitors" --> Replica

    %% Dotted Red Links
    Client2 <-.-> Primary
    Replica <-.-> P
    P <-.-> Orchestrator

    %% Styling for Dotted Links
    linkStyle 5 stroke:red,stroke-width:4px,stroke-dasharray: 5 5
    linkStyle 6 stroke:red,stroke-width:4px,stroke-dasharray: 5 5
    linkStyle 7 stroke:red,stroke-width:4px,stroke-dasharray: 5 5
```

### Split-Brain Prevention

```mermaid
sequenceDiagram
    participant Orchestrator
    participant ClientApps as Client Applications
    participant OldPrimary as Old Primary
    participant Replica
    participant DNS
    
    Orchestrator->>Orchestrator: Pause Failover
    Orchestrator->>ClientApps: Notify to Stop Writes
    ClientApps-->>Orchestrator: Writes Stopped
    Orchestrator->>OldPrimary: Fence/Stop
    Orchestrator->>Replica: Promote to New Primary
    Orchestrator->>DNS: Update DNS
    Orchestrator->>ClientApps: Notify to Restart
    ClientApps->>DNS: Connect to New Primary
```

Sources:

- [How Flipkart Built a Highly Available MySQL Cluster for 150+ Million Users](https://blog.bytebytego.com/p/how-flipkart-built-a-highly-available)
