---
title: "Python's Memory Management"
date: 2025-09-24
type: diagram
tags:
  - python
  - memory
---

### Python's Private Heap

```mermaid
graph TD
    subgraph System Memory
        A[Operating System Memory]
    end

    subgraph Python Process
        B(Python Interpreter)
        subgraph C [Private Heap]
            D[Python Object 1]
            E[Python Object 2]
            F[...]
        end
        B -- Manages --> C
    end

    A -- "Allocates Memory For" --> B
```

### Reference Counting

```mermaid
graph LR
    subgraph ReferenceCounting [Reference Counting]
        subgraph InitialState [Initial State: x = my_object]
            x1(x) --> obj1{Object<br/>ref_count = 1};
        end

        subgraph SecondReference [y = x]
            x2(x) --> obj2{Object<br/>ref_count = 2};
            y2(y) --> obj2;
        end

        subgraph Dereference [del x]
            y3(y) --> obj3{Object<br/>ref_count = 1};
        end

        subgraph FinalState [del y]
             obj4{Object<br/>ref_count = 0};
             G[Memory Freed];
             obj4 -.-> G;
        end

        %% These invisible links force the correct Left-to-Right order
        obj1 ~~~ obj2
        obj2 ~~~ obj3
        obj3 ~~~ obj4
    end
```

### 3. Generational Garbage Collection

This diagram shows the three generations of the garbage collector and how objects can move between them or be collected.

```mermaid
graph LR
    A[New Objects] --> B;

    subgraph Gen0
        B(obj A) -- Survives GC --> C{Promoted};
        D(obj B) -- Collected --> E[Garbage];
    end

    C --> F;

    subgraph Gen1
        F(obj C) -- Survives GC --> G{Promoted};
        H(obj D) -- Collected --> I[Garbage];
    end

    G --> J;

    subgraph Gen2
        J(obj E) -- Long-Lived --> K(obj E);
    end
```
