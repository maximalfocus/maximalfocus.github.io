---
title: "Singleton Pattern"
date: 2025-10-06
type: diagram
tags:
  - singleton
  - design-patterns
---

### The Classic Singleton Pattern

```mermaid
classDiagram
    %% Adding a stereotype to make the pattern role explicit
    class Singleton {
        <<Singleton>>
        -_instance: Singleton$
        -Singleton()
        +getInstance(): Singleton$
    }

    %% The note remains the same and is still very helpful
    note for Singleton "getInstance() logic:\nif _instance is null:\n  _instance = new Singleton()\nreturn _instance"

    class ClientA {
        -singleton_instance: Singleton
        +do_work()
    }
    class ClientB {
        -singleton_instance: Singleton
        +do_something_else()
    }

    ClientA ..> Singleton : uses
    ClientB ..> Singleton : uses
```

### The Anti-Pattern Problem: Global Shared State

```mermaid
graph TD
    %% All relationships are now grouped inside the subgraph
    subgraph Application
        direction TB
        ModuleA -->|Reads/Writes to| Singleton["Singleton (Global State)"];
        ModuleB -->|Reads/Writes to| Singleton;
        ModuleC -->|Reads from| Singleton;

        ModuleA -.-> |Invisible Coupling| ModuleB;
        ModuleB -.-> |Invisible Coupling| ModuleC;
    end

    %% Added styling for the modules to match the image's purple
    style ModuleA fill:#e6e6fa,stroke:#333,stroke-width:2px
    style ModuleB fill:#e6e6fa,stroke:#333,stroke-width:2px
    style ModuleC fill:#e6e6fa,stroke:#333,stroke-width:2px

    %% Kept the original styling for the Singleton
    style Singleton fill:#f9f,stroke:#333,stroke-width:2px
```

### The Multi-threading Race Condition

```mermaid
sequenceDiagram
    participant ThreadA
    participant ThreadB
    participant SingletonClass

    par
        ThreadA->>SingletonClass: getInstance()
        activate SingletonClass
        note over ThreadA, SingletonClass: Checks if instance exists (it's null)
    and
        ThreadB->>SingletonClass: getInstance()
        activate SingletonClass
        note over ThreadB, SingletonClass: Checks if instance exists (it's null)
    end

    note right of SingletonClass: Both threads see a null instance before either can create one.

    par
        ThreadA->>SingletonClass: Creates new Instance A
        SingletonClass-->>ThreadA: Returns Instance A
        deactivate SingletonClass
    and
        ThreadB->>SingletonClass: Creates new Instance B
        SingletonClass-->>ThreadB: Returns Instance B
        deactivate SingletonClass
    end

    note right of SingletonClass: Problem! Two instances are created.
```

### The "Pythonic" Singleton: A Module

```mermaid
graph TD
    subgraph YourApp
        direction TB
        A[main_app.py] -->|import config| C["config.py (Module Singleton)"];
        B[some_other_module.py] -->|import config| C;
    end

    style C fill:#ccf,stroke:#333,stroke-width:2px
```

### The Real Reason: Controlled Instantiation (Lazy Loading)

```mermaid
sequenceDiagram
    participant Client
    participant predict_function
    participant ModelLoader

    Client->>predict_function: Make prediction
    activate predict_function
        predict_function->>ModelLoader: Get Instance
        activate ModelLoader
        note over ModelLoader: First call: instance does not exist.
        ModelLoader->>ModelLoader: __init__() - Loading large model...
        ModelLoader-->>predict_function: Return new instance
        deactivate ModelLoader
        predict_function->>ModelLoader: instance.predict()
    predict_function-->>Client: Return prediction
    deactivate predict_function

    Client->>predict_function: Make another prediction
    activate predict_function
        predict_function->>ModelLoader: Get Instance
        activate ModelLoader
        note over ModelLoader: Instance already exists, return it directly.
        ModelLoader-->>predict_function: Return existing instance
        deactivate ModelLoader
        predict_function->>ModelLoader: instance.predict()
    predict_function-->>Client: Return prediction
    deactivate predict_function
```

### Related Pattern: The Object Pool

```mermaid
sequenceDiagram
    participant Client
    participant ObjectPool
    participant DB_Connection

    Client->>ObjectPool: acquireConnection()
    activate ObjectPool
    alt Pool has an available connection
        ObjectPool-->>Client: return existing_connection
    else Pool is empty and not at max capacity
        ObjectPool->>DB_Connection: new()
        activate DB_Connection
        DB_Connection-->>ObjectPool: new_connection
        deactivate DB_Connection
        ObjectPool-->>Client: return new_connection
    end
    deactivate ObjectPool

    Note over Client: Client uses the connection...

    Client->>ObjectPool: releaseConnection(connection)
    activate ObjectPool
    Note over ObjectPool: Connection is returned to the pool for reuse.
    deactivate ObjectPool
```
