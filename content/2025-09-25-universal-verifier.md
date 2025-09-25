---
title: "Universal Verifier"
date: 2025-09-25
type: diagram
tags:
  - universal-verifier
  - llm
  - ai
  - rlhf
---

### The Core Concept of a Universal Verifier

```mermaid
%% Refined Diagram: Criteria as an Explicit Input to the Verifier
graph TD
    subgraph "The LLM System"
        LLM[("Large Language Model")]
    end

    subgraph "Knowledge Base"
        Criteria["Evaluation Criteria <br> (e.g., Rubrics, Principles)"]
    end

    subgraph "Generation & Evaluation"
        Output["LLM Output <br> (Code, Text, etc.)"]
        Verifier(Universal Verifier)
    end
    
    subgraph "Learning"
        Reward{Comprehensive Reward Signal <br> & Interpretable Critique}
    end
    
    LLM -- Generates --> Output
    Output --> Verifier
    Criteria -- Guides --> Verifier
    Verifier -- Produces --> Reward
    Reward -- Reinforcement Learning --> LLM
    
    style Verifier fill:#f9f,stroke:#333,stroke-width:4px
    style LLM fill:#9cf,stroke:#333,stroke-width:2px
    style Reward fill:#9f9,stroke:#333,stroke-width:2px
    style Criteria fill:#e9e,stroke:#333,stroke-width:2px
```

### Current Paths to Building a Universal Verifier

```mermaid
%% Diagram 2: Current Research Paths to Building a Universal Verifier
graph LR
    A(Start: The Need for<br>Better Evaluation) --> B
    
    subgraph "Path 1: Generative Verifiers (GenRM)"
        B[LLM Output] --> B1(Generative Reward Model)
        B1 --> B2["Generates Natural Language Critique <br> 'The reasoning is sound but<br>the tone is too formal.'"]
        B2 --> B3(Critique is converted<br>to Reward)
    end

    A --> C
    subgraph "Path 2: Rubric-Based Systems (RaR)"
        C[LLM Output] --> C1(Decompose 'Quality' into<br>Rubrics)
        C1 --> C2["- ✅ Clarity <br> - ✅ Empathy <br> - ❌ Conciseness"]
        C2 --> C3(Evaluate against Rubrics for<br>Multi-Dimensional Reward)
    end

    A --> E
    subgraph "Path 3: Pairwise & Bootstrapped RL"
        E["Generate Multiple Outputs <br> (A, B, C)"] --> E1(Randomly Select 'B'<br>as Reference)
        E1 --> E2(Pairwise Comparison <br> Is A better than B? <br> Is C better than B?)
        E2 --> E3(Generate Relative<br>Reward Signal)
    end
```

### Impact on LLM Evolution: The Self-Improvement Loop

```mermaid
%% Diagram with minor refinement for RLHF clarity
graph TD
    subgraph "Future: Autonomous Loop <br>(Fast & Scalable)"
        direction TB
        F_A[LLM Generates Output] --> F_B(Universal Verifier)
        F_B -- Immediate Feedback --> F_C{Generates Perfect<br>Reward Signal}
        F_C --> F_D[Instantly Fine-tunes<br>the LLM]
        F_D --> F_A
        style F_B fill:#f9f,stroke:#333,stroke-width:4px
    end

    subgraph "Current Method: RLHF <br>(Slow, Human in the Loop)"
        direction TB
        C_A[LLM Generates Outputs] --> C_B{Human Annotator}
        C_B --> C_C[Creates Preference Data]
        C_C --> C_D[Trains a separate<br>Reward Model]
        C_D -- Provides Reward Signal --> C_E[Fine-tunes the LLM]
        C_E -.-> C_A
        style C_B fill:#ff9,stroke:#333,stroke-width:2px
    end
```

### The Core Challenge: Who Verifies the Verifier?

```mermaid
%% Diagram 4: The Recursive Challenge of Alignment
graph TD
    A[Humans build Initial<br>Verifier V1] --> B

    subgraph "Autonomous Improvement Cycle"
        B("Verifier V(n) evaluates LLM") --> C("LLM(n) is improved via RL")
        C --> D("Improved LLM(n+1) helps<br>build a better verifier")
        D --> E("Verifier V(n+1) is created")
        E --> B
    end

    E --> F(("Verifier V(n+1) surpasses<br>human evaluation ability"))
    F --> G{How can humans ensure<br>the Verifier remains<br>aligned with our<br>best interests?}

    style G fill:#c33,stroke:#333,stroke-width:2px,color:#fff
```

### Sources

- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://arxiv.org/abs/2408.15240)
- [Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains](https://arxiv.org/abs/2507.17746)
- [Reinforcement Learning with Rubric Anchors](https://arxiv.org/abs/2508.12790)
- [Writing-Zero: Bridge the Gap Between Non-verifiable Tasks and Verifiable Rewards](https://arxiv.org/abs/2506.00103)
- [Learning to Reason without External Rewards](https://arxiv.org/abs/2505.19590)
