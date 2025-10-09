---
title: "ChatGPT's Memory"
date: 2025-09-17
type: diagram
tags:
  - chatgpt
  - memory
  - ai
---

### The Layered Architecture of ChatGPT's Memory

```mermaid
graph TD
    subgraph "User's Device"
        A[User Prompt: What about the weather there in March?]
    end

    subgraph "All Memory Components (Bundled with Every Prompt)"
        B["User Knowledge Memories (AI-Generated & Opaque)"]
        C["<strong>Model Set Context (User-Controlled & Explicit)</strong><br/><em>[Highest Priority]</em>"]
        D["Recent Conversation Content (User's Messages Only)"]
        E["Interaction Metadata (Device, Usage Patterns)"]
    end

    subgraph "Processing by OpenAI"
        F{Large Context Window}
        G[Powerful LLM]
        H[Response: In Tokyo, the weather in March...]
    end

    A --> F
    B --> F
    C --> F
    D --> F
    E --> F
    F --> G
    G --> H

    style C fill:#9d9dff,stroke:#00008B,stroke-width:4px,color:black
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#9cf,stroke:#333,stroke-width:2px
    style E fill:#f99,stroke:#333,stroke-width:2px
```

### The "Bitter Lesson" Approach vs. The Common RAG Assumption

```mermaid
graph LR
    subgraph A ["The Common Assumption (Complex RAG Approach)"]
        direction TB
        A1[User Prompt] --> A2{1.Query Encoder};
        A2 --> A3[2.Vector Database Search];
        A4[Memory Chunks] --> A3;
        A3 --> A5[3.Retrieve Relevant Memories];
        A1 --> A6((Combine));
        A5 --> A6;
        A6 --> A7[LLM];
        A7 --> A8[Response];
    end

    subgraph B ["The 'Bitter Lesson' Approach (As described in the post)"]
        direction TB
        B1[User Prompt] --> B3{Combine All Memories};
        B2[All Memory Components] --> B3;
        B3 --> B4["Massive Context Window
        (LLM does the filtering)"];
        B4 --> B5[Response];

    end

    style A fill:#ffe,stroke:#333,stroke-width:2px
    style B fill:#eff,stroke:#333,stroke-width:2px
```

Sources:

- [ChatGPT Memory and the Bitter Lesson](https://www.shloked.com/writing/chatgpt-memory-bitter-lesson)
