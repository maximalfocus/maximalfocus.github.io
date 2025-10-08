---
title: "Vectorization"
date: 2025-09-27
type: diagram
tags:
  - vectorization
  - ai
---

### The General Vectorization Process

```mermaid
%% General Vectorization Process %%
graph TD;
    A["Unstructured Data <br> (Text, Image, Audio)"] -- "Input" --> B{"Vectorization Model <br> (e.g., BERT, CNN)"};
    B -- "Processes & Encodes" --> C["Numerical Vector<br>Representation <br> [0.12, -0.45, 0.89, ..., -0.21]"];
    C -- "Used for AI Tasks" --> D(Search, Recommendation,<br>Classification);
```

### Text Vectorization Example (Contextual Embeddings)

```mermaid
graph TD;
    A("Input Sentence: <br> 'AI is transforming <br> the world'") --> B{"Transformer Model <br> (eg BERT)"};

    %% --- Define the Left Branch (Inside a Subgraph) --- %%
    subgraph "How it works"
        B_sub1("Tokenization") --> B_sub2("Attention Mechanism") --> B_sub3("Encoder Layers");
    end

    %% --- Define the Right Branch --- %%
    C("Context-Aware <br> Vector Representation") --> D("[0.76, 0.33, -0.15, ..., 0.92]");

    %% --- Create the fork from the central model to each branch --- %%
    B --> B_sub1;
    B --> C;
```

### Image Vectorization via a Convolutional Neural Network (CNN)

```mermaid
%% Image Vectorization via CNN %%
graph LR;
    A["Input Image <br> (Matrix of Pixels)"] --> B["Convolutional Layers <br> (Detect edges, <br> shapes, textures)"];
    B --> C["Pooling Layers <br> (Downsample & <br> summarize features)"];
    C --> D["Flatten Layer <br> (Converts 2D feature <br> maps to 1D)"];
    D --> E["Output Feature Vector <br> [10.4, 2.1, -5.8, ..., 7.7]"];
```

### Semantic Similarity in a Vector Space

```mermaid
%% --- Diagram 1: Similarity Measurement --- %%
graph LR;
    subgraph "Similarity Measurement"
        A["Distance(King, Queen) <br> is small"];
        B["Distance(King, Man) <br> is small"];
        C["Distance(King, Woman) <br> is large"];
    end

%% --- Diagram 2: Vector Operations & Relationships --- %%

    subgraph "Vector Operations & Relationships"
        op1["vector('King') - vector('Man')"] --> op2["+vector('Woman')"] --> op3["≈ vector('Queen')"];
    end

%% --- Diagram 3: High-Dimensional Vector Space --- %%
    subgraph "High-Dimensional <br> Vector Space"
        Man["vector('Man')"]
        King["vector('King')"]
        Woman["vector('Woman')"]
        Queen["vector('Queen')"]

        Man -- "Royal Relationship" --> King;
        Man -- "Gender Relationship" --> Woman;
        Woman -- "Royal Relationship" --> Queen;
        King -- "Gender Relationship" --> Queen;
    end
```
