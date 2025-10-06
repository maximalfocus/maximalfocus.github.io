---
title: "The Parallel Coding Agent Lifestyle"
date: 2025-10-06
type: diagram
tags:
  - ai
  - agents
---

### High-Level Parallel Workflow

```mermaid
graph TD
    A[Developer] --> B{Primary Task: Review & Land Change};
    A --> C{Delegate Parallel Tasks};

    subgraph "Parallel AI Coding Agents"
        D[Agent 1: Research/PoC]
        E[Agent 2: Codebase Comprehension]
        F[Agent 3: Small Maintenance Tasks]
        G[Agent 4: Directed Implementation]
    end

    C --> D;
    C --> E;
    C --> F;
    C --> G;

    D --> H{Review Output};
    E --> H;
    F --> H;
    G --> B;

    B --> I[Merge to Main];
    H --> J[Inform Future Work];
```

### The "Architect and Implementer" Workflow

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Arch as Architect Agent
    participant Impl as Implementer Agent

    Dev->>+Arch: Start Brainstorming for a new feature
    Arch-->>Dev: Asks clarifying questions
    Dev->>Arch: Provides answers and refines idea
    Arch->>Arch: Creates Design Document
    Arch->>Arch: Creates Detailed Implementation Plan
    Arch-->>-Dev: Provides completed plan

    Dev->>+Impl: Start new session with plan
    Impl-->>Dev: Acknowledges plan, asks questions
    Dev->>Arch: Relay questions about plan
    Arch-->>Dev: Provides clarification
    Dev->>Impl: Provides clarification to Implementer

    loop Execution & Review Cycle
        Dev->>Impl: Execute first 3-4 tasks from plan
        Impl->>Impl: Implements code
        Impl-->>Dev: Reports completion of tasks
        Dev->>Arch: Review the work done by Implementer
        Arch-->>Dev: Provides feedback/approval
        Dev->>Impl: Relay feedback for revision
    end

    Dev->>Impl: Create Pull Request on GitHub
    Impl-->>-Dev: Pushes to repo and creates PR

    Note over Dev: External review (e.g., CodeRabbit) is initiated
    Dev->>Impl: Provide external review feedback for final fixes
    Impl->>Impl: Applies final changes
    Dev->>Dev: Final Review & Merge
```

### Key Patterns Mind Map

```mermaid
mindmap
  root((Parallel Coding Agent Lifestyle))
    ::icon(fa fa-cogs)
    (Research for Proof of Concepts)
      ::icon(fa fa-flask)
      - Validate new ideas
      - Test new libraries
      - Build prototypes
    (Codebase Comprehension)
      ::icon(fa fa-search)
      - Explain existing systems
      - Answer questions about code logic
      - Document complex paths
    (Small Maintenance Tasks)
      ::icon(fa fa-wrench)
      - Fix deprecation warnings
      - Resolve minor irritations
      - Low-stakes, low-overhead edits
    (Carefully Specified Work)
      ::icon(fa fa-sitemap)
      - Execute detailed plans
      - Less effort to review
      - "Authoritarian" prompting approach
```

Sources:

- [https://simonwillison.net/2025/Oct/5/parallel-coding-agents/](https://simonwillison.net/2025/Oct/5/parallel-coding-agents/)
- [https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/)
