---
title: "Cross-Agent Attack"
date: 2025-09-25
type: diagram
tags:
  - ai
  - agents
  - cross-agent-attack
  - security
---

### Cross-Agent Attack Chain

```mermaid
sequenceDiagram
    participant Attacker
    participant Agent A (eg Copilot)
    participant ProjectFilesystem
    participant User
    participant Agent B (eg Claude)
    participant UserOS as User's OS

    Attacker->>Agent A: 1. Hijacks with Indirect Prompt Injection
    note over Agent A: Agent A is now compromised

    Agent A->>ProjectFilesystem: 2. Writes malicious config for Agent B

    User->>Agent B: 3. User runs Agent B
    
    Agent B->>ProjectFilesystem: 4. Reads its (now malicious) configuration
    note over Agent B: Agent B is now compromised

    Agent B->>UserOS: 5. Executes arbitrary code (e.g., calc.exe)

    loop Escalation Loop
        Agent B->>ProjectFilesystem: 6. (Optional) Writes malicious config for Agent A
    end
```

### System Vulnerability Architecture

```mermaid
graph TD
    subgraph "Project Environment<br>(e.g., VS Code Workspace)"
        direction LR
        A[Agent A <br> e.g., Copilot]
        B[Agent B <br> e.g., Claude]
        AC(Agent A Config)
        BC(Agent B Config)
        SC(Source Code)
    end

    %% --- Define Node Connections ---
    A -- "Reads/Writes" --> AC
    B -- "Reads/Writes" --> BC
    A -- "Interacts with" --> SC
    B -- "Interacts with" --> SC
    
    %% --- Define the Attack Connections ---
    A -- "Hijacked agent maliciously<br>writes to" --> BC
    B -- "Compromised agent can<br>write back to" --> AC

    %% --- Style Nodes ---
    style A fill:#D2E2FB,stroke:#333,stroke-width:2px
    style B fill:#D2E2FB,stroke:#333,stroke-width:2px

    %% --- Style Links (Corrected) ---
    %% Link 4 is the 5th link defined: A --> BC
    linkStyle 4 stroke:red,stroke-width:2px,stroke-dasharray: 5 5
    %% Link 5 is the 6th link defined: B --> AC
    linkStyle 5 stroke:orange,stroke-width:2px,stroke-dasharray: 5 5
```

Sources:

- [Cross-Agent Privilege Escalation: When Agents Free Each Other](https://embracethered.com/blog/posts/2025/cross-agent-privilege-escalation-agents-that-free-each-other/)
