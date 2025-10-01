---
title: "LLMs Are a Dead End"
date: 2025-10-02
type: diagram
tags:
  - llm
  - ai
  - reinforcement-learning
---

### Mimicry vs. True Understanding

```mermaid
graph TD
    subgraph "Large Language Models (LLMs): The Mimicry Loop"
        direction TB
        A[Internet Text Dataset] --> B{LLM Training};
        B --> C[Predict Next Word];
        C --> D((Generate Text));
        style A fill:#f9f,stroke:#333,stroke-width:2px
    end

    subgraph "Reinforcement Learning (RL): The Experiential Loop"
        direction TB
        E[Environment] -- Sensation/State --> F{RL Agent};
        F -- Action --> E;
        E -- Reward/Feedback --> F;
        style E fill:#ccf,stroke:#333,stroke-width:2px
    end

    subgraph "Sutton's Core Argument"
        direction TB
        G[Mimicking People] --x H(Lacks World Model & Goals);
        I[Learning from Experience] --> J(Develops World Model & Achieves Goals);
    end

    style G fill:#FFDDC1
    style H fill:#FFDDC1
    style I fill:#D4E4F7
    style J fill:#D4E4F7
```

### Revisiting "The Bitter Lesson"

```mermaid
graph LR
    subgraph "Current LLM Approach"
        A[Massive Compute] & B["Massive Human Knowledge <br/> (Internet Text)"] --> C(Powerful LLMs);
    end

    subgraph "Sutton's Predicted Future (The Bitter Lesson Applied)"
        D[Massive Compute] & E["Learning from Raw Experience <br/> (Interaction, Trial & Error)"] --> F(More Scalable & Capable AI);
    end

    C -- "Will be Superseded by" --> F;

    style A fill:#D4E4F7
    style B fill:#FFDDC1
    style E fill:#D4E4F7
```

### The Continual Learning Agent

```mermaid
graph TD
    subgraph "The Experiential Paradigm (Refined)"
        direction LR
        A(Agent)
        B(Environment)

        A -- "Action" --> B;
        B -- "Sensation & Reward" --> A;

        subgraph "Agent's Internal Components"
            C["Policy<br/>(What to do)"]
            D["Value Function<br/>(How well it's going)"]
            E["World Model<br/>(Predicts consequences)"]
        end

        A --> C
        A --> D
        A --> E

        B -- "Updates" --> E
        D -- "Guides" --> C
        
        %% --- New Connections ---
        E -- "Enables Planning to Refine" --> C;
        E -- "Provides Simulated Experience to Improve" --> D;
    end

    style B fill:#ccf,stroke:#333,stroke-width:2px
    style A fill:#f9f,stroke:#333,stroke-width:2px
```

Source: [Richard Sutton – Father of RL thinks LLMs are a dead end](https://www.youtube.com/watch?v=21EYKqUsPfg)
