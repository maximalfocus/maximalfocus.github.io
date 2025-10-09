---
title: "Reinforcement Learning (RL)"
date: 2025-10-09
type: diagram
tags:
  - reinforcement-learning
  - rl
  - ai
---

### 1. The Core Reinforcement Learning Loop

```mermaid
graph TD
    subgraph Agent
        Policy
        Action
    end

    subgraph Environment
        StateReward[State & Reward]
    end

    %% Define the correct flow of the loop
    StateReward -- Observes --> Policy
    Policy -- Decides --> Action
    Action -- Affects --> StateReward

    %% Add styling to match the original image
    style Agent fill:#f9f,stroke:#333,stroke-width:2px
    style Environment fill:#ccf,stroke:#333,stroke-width:2px
```

### 2. Markov Decision Process (MDP)

```mermaid
graph TD
    %% 1. Define all nodes first
    RL(Reinforcement Learning)
    
    AC(Actor-Critic)
    PB(Policy-Based)
    VB(Value-Based)
    
    DDPG(DDPG)
    SAC(Soft Actor-Critic)
    
    PG(Policy Gradient)
    TRPO(TRPO)
    PPO(PPO)
    
    QL(Q-Learning)
    DQN(Deep Q-Networks)

    %% 2. Group algorithm nodes into their respective subgraphs
    subgraph sg_ac [Actor-Critic]
        DDPG
        SAC
    end
    
    subgraph sg_pb [Policy-Based]
        PG
        TRPO
        PPO
    end
    
    subgraph sg_vb [Value-Based]
        QL
        DQN
    end
    
    %% 3. Define all connections between the nodes
    RL --> AC
    RL --> PB
    RL --> VB
    
    AC --> DDPG
    AC --> SAC
    
    PB --> PG
    PG --> TRPO & PPO
    
    VB --> QL & DQN
    
    %% 4. Define and apply styling for the subgraphs
    classDef yellowBox fill:#ffffe0,stroke:#a8a8a8,stroke-width:1px;
    class sg_ac,sg_pb,sg_vb yellowBox;
```

### 3. Taxonomy of RL Algorithms

```mermaid
graph TD
    RL(Reinforcement Learning)
    VB(Value-Based)
    PB(Policy-Based)
    AC(Actor-Critic)

    RL --> VB
    RL --> PB
    RL --> AC

    subgraph Value-Based
        direction LR
        QL(Q-Learning)
        DQN(Deep Q-Networks)
    end

    subgraph Policy-Based
        direction LR
        PG(Policy Gradient)
        TRPO(TRPO)
        PPO(PPO)
    end

    subgraph Actor-Critic
        direction LR
        DDPG(DDPG)
        SAC(Soft Actor-Critic)
    end

    VB --> QL
    VB --> DQN
    PB --> PG
    PG --> TRPO & PPO
    AC --> DDPG
    AC --> SAC
```

### 4. Actor-Critic Architecture

```mermaid
graph LR

    %% 1. Define subgraphs and their contents
    subgraph sg_interaction [Interaction]
        Environment
    end

    subgraph sg_agent [Agent]
        %% No internal direction needed; it will inherit LR
        Critic("Critic<br>Value Function Q or V")
        Actor("Actor<br>Policy π")
    end

    %% 2. Define all connections between components
    Environment -- State --> Actor
    Actor -- Action --> Environment
    Environment -- "State, Reward" --> Critic
    Critic -- "TD Error / Advantage" --> Actor

    %% 3. Define and apply styling for the subgraphs
    classDef pinkBox fill:#fce8f5,stroke:#333,stroke-width:2px;
    classDef yellowBox fill:#ffffe0,stroke:#a8a8a8,stroke-width:1px;
    
    class sg_agent pinkBox;
    class sg_interaction yellowBox;
```

### 5. Deep Q-Network (DQN) Architecture

```mermaid
graph LR

    %% 1. Define the subgraphs and their internal nodes
    subgraph sg_loop [Loop]
        Env(Environment)
    end

    subgraph sg_agent [DQN Agent]
        QNet(Q-Network)
        TargetNet(Target Network)
        ReplayBuffer[(Replay Buffer)]
    end

    %% 2. Define all connections between the components
    Env -- State --> QNet
    QNet -- Action --> Env
    Env -- "(s, a, r, s')" --> ReplayBuffer
    ReplayBuffer -- "Sample Batch" --> QNet
    TargetNet -- "Provides Target Q-value" --> QNet
    QNet -- "Periodically copies weights" --> TargetNet

    %% 3. Define and apply styling for the subgraphs
    classDef yellowBox fill:#ffffe0,stroke:#a8a8a8,stroke-width:1px;
    class sg_loop,sg_agent yellowBox;

    %% 4. Style the specific links based on their definition order
    %% Link 4 (5th link defined) is the Target -> QNet connection
    %% Link 5 (6th link defined) is the QNet -> Target connection
    linkStyle 4 stroke:blue,stroke-width:2px;
    linkStyle 5 stroke:red,stroke-width:2px,stroke-dasharray:5 5;
```

- DDPG: Deep Deterministic Policy Gradient
- TRPO: Trust Region Policy Optimization
- PPO: Proximal Policy Optimization
- TD Error: Temporal Difference Error
- DQN: Deep Q-Network
