---
title: "Building Your Own Deep Research with Exa"
date: 2025-09-23
type: diagram
tags:
  - research
  - ai
  - agents
---


### Traditional vs. AI-Powered User Research Process

```mermaid
graph TD;
    subgraph AI-Powered User Research
        direction TB
        A1[Start: User Question] --> A2[AI Generated Questions];
        A2 --> A3[AI Participant Personas];
        A3 --> A4[AI Simulated Interviews];
        A4 --> A5[AI Powered Analysis];
        A5 --> A6[Finish: Final User Research Report];
    end

    subgraph Traditional User Research
        direction TB
        B1[Start: User Question] --> B2[Create Interview Questions];
        B2 --> B3["Identify & Recruit<br/>Participants (2-3 weeks)"];
        B3 --> B4["Conduct Interviews<br/>(1-2 weeks)"];
        B4 --> B5["Analyze Responses<br/>(1 week)"];
        B5 --> B6[Finish: Final User Research Report];
    end

    style A1 fill:#e6e6fa,stroke:#8a2be2
    style A2 fill:#e6e6fa,stroke:#8a2be2
    style A3 fill:#e6e6fa,stroke:#8a2be2
    style A4 fill:#e6e6fa,stroke:#8a2be2
    style A5 fill:#e6e6fa,stroke:#8a2be2
    style A6 fill:#90ee90,stroke:#006400

    style B1 fill:#e6e6fa,stroke:#8a2be2
    style B2 fill:#e6e6fa,stroke:#8a2be2
    style B3 fill:#ff6347,stroke:#b22222
    style B4 fill:#ff6347,stroke:#b22222
    style B5 fill:#ff6347,stroke:#b22222
    style B6 fill:#e6e6fa,stroke:#8a2be2
```

### AI-Powered Deep Research Workflow

```mermaid
graph TD;
    A[Research Question] --> B["Tool Calling (Web Search)<br/>- Exa"];
    B --> C["Retrieval Augmented<br/>Generation (RAG)"];
    C --> D["Large Language Model<br/>(LLM) - Cerebras"];
    D --> E[Answer];

    style A fill:#FFDDF4,stroke:#A020F0,stroke-width:2px
    style B fill:#BF40BF,stroke:#8A2BE2,stroke-width:2px,color:#fff
    style C fill:#BF40BF,stroke:#8A2BE2,stroke-width:2px,color:#fff
    style D fill:#FFDDF4,stroke:#A020F0,stroke-width:2px
    style E fill:#98FB98,stroke:#3CB371,stroke-width:2px
```

### Advanced Multi-Layer Research Process

```mermaid
graph TD;
    subgraph Advanced Research
        direction TB
        A[Research Question] --> B{Layer 1: Initial Search};
        B --> C{"Get Initial Analysis &<br/>Identify Follow-up Topic"};
        C --> D{Layer 2: Follow-up Search};
        D --> E{Final Synthesis};
        E --> F[Comprehensive Analysis];
    end

    style A fill:#e6e6fa,stroke:#8a2be2,stroke-width:2px
    style B fill:#e6e6fa,stroke:#8a2be2,stroke-width:2px
    style C fill:#e6e6fa,stroke:#8a2be2,stroke-width:2px
    style D fill:#e6e6fa,stroke:#8a2be2,stroke-width:2px
    style E fill:#e6e6fa,stroke:#8a2be2,stroke-width:2px
    style F fill:#98FB98,stroke:#3CB371,stroke-width:2px
```

### Anthropic Multi-Agent System

```mermaid
graph TD;
    subgraph Anthropic Multi-Agent System
        direction TB
        A["Lead Agent: Decomposes<br/>Query into Subtasks"] --> B["Subagent 1: Researches<br/>Core Concepts"];
        A --> C["Subagent 2: Researches<br/>Latest Developments"];
        A --> D["Subagent 3: Researches<br/>Applications"];
        B --> E{"Lead Agent: Synthesizes All<br/>Findings"};
        C --> E;
        D --> E;
        E --> F["Final Comprehensive<br/>Report"];
    end

    style A fill:#4682B4,stroke:#333,stroke-width:2px,color:white
    style B fill:#B0C4DE,stroke:#333,stroke-width:2px,color:black
    style C fill:#B0C4DE,stroke:#333,stroke-width:2px,color:black
    style D fill:#B0C4DE,stroke:#333,stroke-width:2px,color:black
    style E fill:#4682B4,stroke:#333,stroke-width:2px,color:white
    style F fill:#98FB98,stroke:#333,stroke-width:2px,color:black
```

Source: [How to Build Advanced AI Agents](https://www.youtube.com/watch?v=B0TJC4lmzEM)
