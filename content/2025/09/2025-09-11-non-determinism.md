---
title: "Defeating Nondeterminism in LLM Inference"
date: 2025-09-11
type: diagram
tags:
  - non-determinism
  - ai
  - llm
---

### The Root Cause of Non-Determinism

```mermaid
graph TD
    A["User Experience:<br/>Non-Deterministic Output<br/>(Different results for the<br/>same query)"] --> B{Why does this happen?};
    B --> C["LLM Inference Server uses<br/>Dynamic Batching"];
    C --> D[Batch size changes constantly<br/>based on server load];
    D --> E{Core Issue: Lack of 'Batch<br/>Invariance' in GPU Kernels};
    E --> F["The kernel changes its computation strategy<br/>(e.g., how it sums numbers)<br/>based on batch size"];
    F --> G[This changes the order of<br/>floating-point math<br/>operations];
    G --> H["Fundamental Property:<br/>Floating-point math is not associative<br/>(a + b) + c ≠ a + (b + c)"];
    H --> I[Tiny numerical differences<br/>appear and accumulate];
    I --> A;

    style E fill:#f9f,stroke:#333,stroke-width:2px
```

### How Different Batch Sizes Lead to Different Outputs

```mermaid
flowchart TD
    subgraph "Two Identical User Requests"
        Req1(Request 1)
        Req2(Request 2)
    end

    Req1 --> Server1{Server is busy}
    Req2 --> Server2{Server is idle}

    Server1 --> Batch1[Processed in a LARGE batch]
    Server2 --> Batch2[Processed in a SMALL batch]

    Batch1 --> Kernel1[Kernel splits calculation<br/>across many cores for<br/>efficiency]
    Batch2 --> Kernel2["Kernel uses a different<br/>(less parallel) calculation<br/>path"]

    Kernel1 --> Ops1["Math Order A:<br/>(a+b) + (c+d)"]
    Kernel2 --> Ops2["Math Order B:<br/>((a+b) + c) + d"]

    Ops1 --> Result1[Result is 1.234567]
    Ops2 --> Result2[Result is 1.234568]

    Result1 --> Output1["Final Output A"]
    Result2 --> Output2["Final Output B"]
```

### The Solution and Experimental Proof

```mermaid
graph TD
    subgraph "Problem"
        P[Non-Deterministic LLM<br/>Inference]
    end

    subgraph "Proposed Solution"
        S[Engineer 'Batch-Invariant'<br/>Kernels]
        S_Desc["This forces the kernel to use the <b>same</b> computation path<br/>and math order, no matter<br/>the batch size."]
        S --> S_Desc
    end

    subgraph "Experiment: 1 Prompt, 1000 Requests"
        Before["<b>Before (Default Kernels)</b>"] --> Result_Before["<b>Result: 80 Unique Outputs</b><br/>(Non-Deterministic)"]
        After["<b>After (Batch-Invariant<br/>Kernels)</b>"] --> Result_After["<b>Result: 1 Identical Output</b><br/>(Deterministic!)"]
    end

    P --> S
    S --> After

    style Result_Before fill:#fbb,stroke:#333,stroke-width:2px
    style Result_After fill:#bbf,stroke:#333,stroke-width:2px
```

Sources:

- [Defeating Nondeterminism in LLM Inference](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
