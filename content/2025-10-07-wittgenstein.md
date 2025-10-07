---
title: "Tractatus Logico-Philosophicus vs Language-Games"
date: 2025-10-07
type: diagram
tags:
  - wittgenstein
  - philosophy
---

### The Meaning of a Word

```mermaid
graph TD
    A[Word] --> B{How is meaning determined?};
    
    B -- "<b>Correct (Language-Games)</b><br>Meaning is Use" --> C[Use in an Activity];
    B -. "<b>Incorrect (Tractatus)</b><br>Meaning is Reference" .-> D(x Object x);

    style C fill:#e6ffed,stroke:#2a6e3d,stroke-width:2px
    style D fill:#ffe6e6,stroke:#a33,stroke-width:2px,color:#a33
```

### Mixing Language Games

```mermaid
graph TD
    subgraph "Basketball Language-Game"
        A("Statement:<br>'Grab the boards!'")
    end

    subgraph "Physics Language-Game"
        B("Underlying Rule/Fact:<br>'A solid object is mostly empty space.'")
    end

    C{Misapplication of Rules};

    A -- "is judged by rules from..." --> C;
    B -- "...the Physics Language-Game" --> C;
    
    C --> D["Result: Meaningless Confusion<br><i>(e.g., 'But he didn't even touch the wooden backboard!')</i>"];

    style D fill:#ff9999,stroke:#a33,stroke-width:2px;
```

### No Super Language

```mermaid
graph TD
    subgraph "<b>Incorrect (Tractatus):</b> A Single 'Super Language' Governs All"
        direction TB
        A(Universal Logical Language) --> B(Science);
        A --> C(Ethics);
        A --> D(Poetry);
    end

    subgraph "<b>Correct (Language-Games):</b> A Web of Equal, Autonomous Games"
        direction TB
        E(Science) --- F(Woodworking);
        F --- G(Religion);
        G --- H(Jokes);
        H --- E;
        E --- G;
    end

    linkStyle 4 5 6 7 8 stroke-width:2px,stroke:blue,stroke-dasharray: 5 5;
```

### The Function of Language: Picture vs. Toolbox

```mermaid
graph TD
    subgraph "Tractatus: Picture Theory of Language"
        direction TB
        A[Word] -->|Represents| B((Object in Reality));
        C[Proposition] -->|Pictures| D((State of Affairs));
        E((<b>Core Idea:</b><br>Language has ONE primary function:<br>to state facts.));
    end

    subgraph "Language-Games: Meaning is Use"
        direction TB
        F[Word] --> G{Used in a context...};
        G --> H["Ordering ('Water!')"];
        G --> I["Describing ('The water is cold.')"];
        G --> J["Questioning ('Water?')"];
        K((<b>Core Idea:</b><br>Language is a toolbox with MANY functions.));
    end
```

### The Structure of Language: A Single Logic vs. Countless Games

```mermaid
graph TD
    subgraph "Tractatus: A Single, Ideal Structure"
        direction TB
        A(Universal Logical Form) --> B(Language A);
        A --> C(Language B);
        A --> D(Language C);
        E[All language is reducible to a single, rigid logic.]
    end

    subgraph "Language-Games: A Network of Activities"
        direction TB
        F((Science)) --- G((Religion));
        G --- H((Jokes));
        H --- I((Poetry));
        I --- F;
        G --- I;
        J[Language is a web of diverse, overlapping practices with no single center.]
    end
```

### The Nature of Concepts: Essence vs. Family Resemblance

```mermaid
graph TD
    subgraph "Tractatus: The Search for Essence"
        direction TB
        A["Concept: 'Game'"] --> D{"The Shared Essence of 'Game-ness'"};
        B["Board Games"] --> D;
        C["Card Games"] --> D;
        E["Ball Games"] --> D;
    end

    subgraph "Language-Games: Family Resemblance"
        direction TB
        F["Board Games"] --- |"Rules, Competition"| G["Card Games"];
        G --- |"Skill, Luck"| H["Ball Games"];
        H --- |"Physical Activity, Rules"| F;
        I["No single feature is common to ALL, but a network of overlapping traits links them."];
    end
```

### The Role of Philosophy: Architect vs. Therapist

```mermaid
graph TD
    subgraph "Tractatus: Philosophy as Construction"
        direction TB
        A(Philosopher as Architect) -->|Builds| B(A Perfect Logical Framework);
        B -->|To Solve| C(Metaphysical Problems);
        C --> D{Final Answer};
    end

    subgraph "Language-Games: Philosophy as Therapy"
        direction TB
        E(Philosopher as Therapist) -->|Untangles| F(A Knot of Linguistic Confusion);
        F -->|To Dissolve| G(The Metaphysical 'Problem');
        G --> H{The Problem Disappears};
    end
```
