---
title: "Quantization"
date: 2025-10-09
type: diagram
tags:
  - quantization
  - ai
---

### 1. The Core Quantization and Dequantization Process

```mermaid
graph TD
    %% Define styles for input/output and processing nodes
    classDef inputOutput fill:#cde4ff,stroke:#333,stroke-width:2px;
    classDef process fill:#f9f9f9,stroke:#333,stroke-width:1px;

    subgraph Quantization
        A[FP32 Value] --> B[Divide by Scale];
        B --> C[Add Zero-Point];
        C --> D[Round to Nearest Integer];
        D --> E[INT8/INT4 Value];
    end

    subgraph Dequantization
        F[INT8/INT4 Value] --> G[Subtract Zero-Point];
        G --> H[Multiply by Scale];
        H --> I[Approximated FP32 Value];
    end

    %% Link the two processes
    E --> F;

    %% Apply styles
    class A,I inputOutput;
    class E,F inputOutput;
    class B,C,D,G,H process;
    linkStyle 4 stroke:#ff9999,stroke-width:2px,fill:none;
```

### 2. Symmetric vs. Asymmetric Quantization

```mermaid
graph TD
    subgraph "Symmetric Quantization <br>(for Weights)"
        direction TB
        A[FP32 Range: -1.0 to 1.0] --> B["Zero-Point = 0"];
        B --> C[INT8 Range: -127 to 127];
        style A fill:#cde4ff
        style C fill:#d5e8d4
    end

    subgraph "Asymmetric Quantization <br>(for Activations)"
        direction TB
        D[FP32 Range: 0.0 to 2.5] --> E["Zero-Point = 60 (Example)"];
        E --> F[INT8 Range: 0 to 255];
        style D fill:#cde4ff
        style F fill:#d5e8d4
    end
```

### 3. Comparison of Quantization Strategies: PTQ vs. QAT

```mermaid
graph TD
    subgraph "Post-Training Quantization <br>(PTQ)"
        direction TB
        A(FP32 Pre-Trained Model) --> B[Calibration with Data];
        B --> C[Calculate Quantization Params];
        C --> D(Quantized <br>INT8/INT4 Model);
    end

    subgraph "Quantization-Aware Training <br>(QAT)"
        direction TB
        E(FP32 Pre-Trained Model) --> F{Fine-Tuning Loop};
        F -- Forward Pass --> G(Simulate Quantization);
        G -- Backward Pass --> H(Update FP32 Weights);
        H --> F;
        F -- End of Fine-Tuning --> I(Final Quantized <br>INT8/INT4 Model);
    end
```

### 4. Overview of Advanced PTQ Techniques

```mermaid
mindmap
  root((Advanced PTQ))
    GPTQ
      ::icon(fa fa-compress)
      Layer-by-layer quantization
      Uses second-order info (Hessian)
      Updates remaining weights <br> to compensate for <br> quantization error
    AWQ
      ::icon(fa fa-star)
      Activation-Aware Weight <br> Quantization
      Identifies important <br> weights based on <br> activation magnitudes
      Protects salient weights <br> with per-channel scaling
    SmoothQuant
      ::icon(fa fa-sliders)
      Addresses challenging <br> activation outliers
      Shifts quantization <br> difficulty from activations <br> to weights
      Enables accurate W8A8 <br> quantization
```

### 5. Hardware Acceleration for Quantized Models

```mermaid
graph TD
    subgraph Standard Inference
        direction TB
        A(FP32 Model) --> B(General-Purpose Cores / <br>CUDA Cores);
        B --> C(Slower Inference);
    end

    subgraph Accelerated Inference
        direction TB
        D(Quantized INT8/INT4 Model) --> E(Specialized Hardware <br><i>e.g., NVIDIA Tensor Cores, <br>Intel AMX</i>);
        E --> F(<b>Faster Inference</b>);
    end

    style F fill:#d5e8d4,stroke:#333,stroke-width:2px
```
