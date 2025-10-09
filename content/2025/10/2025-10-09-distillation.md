---
title: "Distillation"
date: 2025-10-09
type: diagram
tags:
  - distillation
  - ai
---

### 1. The Core Teacher-Student Paradigm

```mermaid
graph TD
    subgraph "Inference/Deployment"
        direction TB
        F[New Input] --> G((Efficient Student LLM));
        G --> H["Fast & Compact Prediction"];
        H --> I[Output];
    end

    subgraph "Training Process"
        direction TB
        subgraph "Teacher Path"
            direction TB
            A[Large Teacher LLM] --> GenSoft["Generates Soft Labels<br/>(Logits)"];
            GenSoft --> C{Distillation Loss};
        end
        subgraph "Data Path"
            direction TB
            B[Training Data & Hard Labels] --> SupLearn["Supervised Learning"];
            SupLearn --> D{Supervised Loss};
        end
        C -- "Guides Student" --> E[Small Student LLM];
        D -- "Trains Student" --> E;
    end

    %% Styling
    style A fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px
    style B fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    style F fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    style I fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    style C fill:#f8cecc,stroke:#b85450,stroke-width:2px
    style D fill:#f8cecc,stroke:#b85450,stroke-width:2px
    style E fill:#d5e8d4,stroke:#82b366,stroke-width:2px
    style G fill:#d5e8d4,stroke:#82b366,stroke-width:2px
```

### 2. The Distillation Loss Function

```mermaid
graph TD
    subgraph "Loss Calculation"
        direction TB
        A[Teacher Logits] -- "Softmax with Temperature (T)" --> B(Teacher's Soft Probabilities);
        C[Student Logits] -- "Softmax with Temperature (T)" --> D(Student's Soft Probabilities);
        B & D -- "KL Divergence" --> E((Distillation Loss));

        F[Student Logits] -- "Standard Softmax" --> G(Student's Hard Predictions);
        H[Ground Truth Labels] --> I((Supervised Loss / Cross-Entropy));
        G -- "Compares with" --> I;

        E -- "Weight (1-α)" --> J{Total Loss};
        I -- "Weight (α)" --> J;
        J -- "Backpropagates to" --> K[Student Model];
    end

    style K fill:#d5e8d4,stroke:#82b366,stroke-width:2px
```

### 3. Comparison of Distillation Techniques

```mermaid
graph TD
    subgraph "Teacher Model"
        T_Input[Input] --> T_L1[Layer 1] --> T_L2[...];
        T_L2 --> T_LN[Final Layer] --> T_Logits[Output Logits];
    end

    subgraph "Student Model"
        S_Input[Input] --> S_L1[Layer 1] --> S_L2[...];
        S_L2 --> S_LN[Final Layer] --> S_Logits[Output Logits];
    end

    subgraph "Distillation Types"
        T_Logits -- "1.Response-Based Distillation (Mimic final output)" --> S_Logits;
        T_L2 -- "2.Feature-Based Distillation (Match intermediate representations)" --> S_L2;
    end

    style T_Logits fill:#f8cecc,stroke:#b85450,stroke-width:2px
    style S_Logits fill:#f8cecc,stroke:#b85450,stroke-width:2px
    style T_L2 fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
    style S_L2 fill:#e1d5e7,stroke:#9673a6,stroke-width:2px
```

### 4. Advanced Distillation Strategies

#### Multi-Teacher Distillation
```mermaid
graph TD
    subgraph "Teacher Ensemble"
        direction TB
        T1[Teacher 1] -->|Logits| C{Combine/Average};
        T2[Teacher 2] -->|Logits| C;
        T3[Teacher N] -->|Logits| C;
    end

    C -- "Aggregated Soft Labels" --> Loss;
    Student[Student Model] -->|Student Logits| Loss((Distillation Loss));
    Loss -- "Trains" --> Student;

    style Student fill:#d5e8d4,stroke:#82b366,stroke-width:2px
```

#### Self-Distillation
```mermaid
graph TD
    subgraph "Phase 1: Teacher Prediction"
        A["Original Model<br>(Teacher)"] -- "Predicts on Unlabeled Data" --> B(Soft Labels);
    end

    subgraph "Phase 2: Student Training"
        C["Same Model<br>(Student)"] -- "Trains on" --> B;
        D[Original Labeled Data] -- "Also Trains" --> C;
    end
    B -- "Knowledge Transfer" --> C
    A -.-> C

    style A fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px
    style C fill:#dae8fc,stroke:#6c8ebf,stroke-width:2px,stroke-dasharray: 5 5
```
