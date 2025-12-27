---
title: "The Evolution of Network Architectures"
date: 2025-12-27
type: post
tags:
    - architecture
---

### Centralized Architecture (The App Model)

```mermaid
graph TD
    %% Define Styles for visual clarity
    classDef user fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef platform fill:#eceff1,stroke:#37474f,stroke-width:3px;
    classDef lockedData fill:#ffcdd2,stroke:#b71c1c,stroke-width:2px,stroke-dasharray: 5 5;
    classDef invisible fill:none,stroke:none;

    %% The Users (Clients)
    UserA((User A)):::user
    UserB((User B)):::user
    UserC((User C)):::user

    %% The Centralized Infrastructure
    subgraph WalledGarden ["🏰 The Centralized Platform (e.g., Twitter/X)"]
        direction TB
        
        Gatekeeper[Gatekeeper / API]:::platform
        Algorithm[Feed Algorithms]:::platform

        %% The Locked Data Silo
        subgraph DataSilo ["🔒 Proprietary Data Silo"]
            DB[(Master DB)]:::lockedData
            Identity[Identity / Handle]:::lockedData
            Graph[Social Graph]:::lockedData
            
            DB --- Identity
            DB --- Graph
        end

        Gatekeeper --> Algorithm --> DB
    end

    %% Connections
    UserA -->|Login & Post| Gatekeeper
    UserB -->|Read Feed| Gatekeeper
    UserC -->|Interaction| Gatekeeper

    %% Visualizing the barrier
    UserA -.-x|No Direct Connection| UserB

    %% Key Insight Note
    NoteNode[/"KEY INSIGHT:<br/>Feudalism Model.<br/>Users rent their identity.<br/>Platform owns the graph."/]:::invisible
    
    DataSilo -.- NoteNode
```

### Federated Architecture (The Email/Mastodon Model)

```mermaid
graph TD
    %% Styles
    classDef user fill:#e1f5fe,stroke:#01579b,stroke-width:2px;
    classDef server fill:#fff3e0,stroke:#e65100,stroke-width:3px;
    classDef s2sConnection stroke:#d84315,stroke-width:4px,stroke-dasharray: 5 5;
    classDef note fill:#fff9c4,stroke:#fbc02d,stroke-dasharray: 5 5;

    %% --- Instance 1 (The Big Giant, e.g., Gmail/Social.co) ---
    subgraph InstanceA ["🏰 Instance A (e.g., Gmail)"]
        ServerA[Server Admin A]:::server
        User1((User 1)):::user
        User2((User 2)):::user
        
        %% Identity Lock-in
        ID_A[Identity: @user1@A]:::note
        
        User1 -->|Trusts| ServerA
        User2 -->|Trusts| ServerA
        User1 -.- ID_A
    end

    %% --- Instance 2 (The Small Rebel) ---
    subgraph InstanceB ["🏯 Instance B (Small Server)"]
        ServerB[Server Admin B]:::server
        User3((User 3)):::user
        
        ID_B[Identity: @user3@B]:::note
        
        User3 -->|Trusts| ServerB
        User3 -.- ID_B
    end

    %% --- Instance 3 (Another Server) ---
    subgraph InstanceC ["🏯 Instance C"]
        ServerC[Server Admin C]:::server
    end

    %% --- The Problem: Server-to-Server Complexity ---
    ServerA <-->|Complex S2S Sync| ServerB
    ServerB <-->|Complex S2S Sync| ServerC
    ServerC <-->|Complex S2S Sync| ServerA

    %% Visualizing the 'Defederation' risk
    linkStyle 3,4,5 stroke:#d84315,stroke-width:4px;

    %% Key Insights
    Insight[/"KEY INSIGHT:<br/>Oligopoly Risk.<br/>If Server A blocks Server B,<br/>User 1 cannot talk to User 3."/]:::note

    ServerA -.- Insight
```

### P2P Architecture (The "Pure" Model)

```mermaid
graph TD
    %% Styles
    classDef mobile fill:#e1f5fe,stroke:#90a4ae,stroke-width:2px,stroke-dasharray: 5 5;
    classDef superpeer fill:#fff9c4,stroke:#fbc02d,stroke-width:4px;
    classDef offline fill:#eceff1,stroke:#cfd8dc,stroke-width:1px,color:#b0bec5;

    %% --- The Mesh Network ---
    
    %% The "Weak" Peers (Mobile Devices)
    PeerA(User A<br/>Mobile/4G):::mobile
    PeerB(User B<br/>Mobile/Offline):::offline
    PeerC(User C<br/>Laptop):::mobile

    %% The "Superpeer" (The Accidental Server)
    SuperPeer{{User D<br/>High Bandwidth<br/>Always Online}}:::superpeer

    %% Connections
    PeerA <-->|Syncs slowly| PeerC
    PeerA -.->|Cannot connect| PeerB
    
    %% The Gravity Well
    PeerA <==>|Relies on| SuperPeer
    PeerC <==>|Relies on| SuperPeer
    SuperPeer -.->|Stores data for| PeerB

    %% Key Insight
    Note[/"KEY INSIGHT:<br/>Physics limits P2P.<br/>'Superpeers' emerge naturally.<br/>We reinvented servers!"/]:::invisible
    
    SuperPeer --- Note

    classDef invisible fill:none,stroke:none;
```

### Nostr Architecture (The Relay Model)

```mermaid
graph TD
    %% Styles
    classDef clientA fill:#b9f6ca,stroke:#00c853,stroke-width:3px;
    classDef clientB fill:#80d8ff,stroke:#0091ea,stroke-width:3px;
    classDef relay fill:#eeeeee,stroke:#bdbdbd,stroke-width:2px,stroke-dasharray: 5 5;
    classDef sharedRelay fill:#fff59d,stroke:#fbc02d,stroke-width:4px;
    classDef key fill:#ffd54f,stroke:#ff8f00,stroke-width:1px,shape:rect;

    %% --- The Sovereign Clients ---
    subgraph Clients ["👥 The Sovereign Users"]
        direction LR
        
        subgraph UserASpace [User A Space]
            UserA((Alice)):::clientA
            KeyA[/"🔑 Key A"/]:::key
        end
        
        subgraph UserBSpace [User B Space]
            UserB((Bob)):::clientB
            KeyB[/"🔑 Key B"/]:::key
        end
    end

    %% --- The Dumb Infrastructure ---
    subgraph Cloud ["☁️ The Dumb Relay Cloud"]
        Relay1[(Relay 1)]:::relay
        
        %% THE MAGIC HAPPENS HERE
        Relay2[(Relay 2<br/>'The Meeting Point')]:::sharedRelay
        
        Relay3[(Relay 3)]:::relay
    end

    %% --- Connections (The Logic) ---
    
    %% Alice Writes to 1 & 2
    UserA -->|Publishes Event| Relay1
    UserA -->|Publishes Event| Relay2
    
    %% Bob Reads from 2 & 3
    Relay2 -.->|Subscribes/Pulls| UserB
    Relay3 -.->|Subscribes/Pulls| UserB

    %% Alice and Bob do NOT touch Relay 3 and 1 respectively
    UserA ~~~ Relay3
    Relay1 ~~~ UserB

    %% --- The Critical "Anti-Federation" Visual ---
    Relay1 -.-x|NO CONNECTION| Relay2
    Relay2 -.-x|NO CONNECTION| Relay3
    
    %% Insight
    Note[/"KEY INSIGHT:<br/>Communication happens because<br/>users overlap on Relay 2.<br/>The Relays don't talk!"/]:::invisible
    
    Relay2 --- Note

    classDef invisible fill:none,stroke:none;
```

### Summary

- **Centralized:** Identity is captive. All roads lead to one database; you serve the platform.
- **Federated:** Complexity kills. Servers must talk to servers (N^2), creating a maintenance nightmare that favors the big players.
- **P2P:** Physics interferes. Mobile devices are too weak to be servers, so the network naturally recentralizes around strong nodes.
- **Nostr:** Architecture is decoupled. Relays are "dumb pipes" that don't talk to each other; intelligence and control reside entirely with the user.

### Sources

- [Nature's many attempts to evolve a Nostr](https://newsletter.squishy.computer/p/natures-many-attempts-to-evolve-a)
