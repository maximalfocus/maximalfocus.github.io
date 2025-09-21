---
title: "Caching Strategies"
date: 2025-09-06
type: diagram
tags:
  - caching-strategies
  - performance
  - latency
---

### Read-intensive application caching strategies

#### Cache-aside

```mermaid
sequenceDiagram
    participant App
    participant Cache
    participant DataStore

    App->>Cache: 1. Read from cache
    Cache-->>App: Cache Miss
    App->>DataStore: 2. Read from data store
    DataStore-->>App: Data
    App->>Cache: 3. Store in cache
    App->>App: 4. Return to app
```

#### Read-through

```mermaid
sequenceDiagram
    participant App
    participant Cache
    participant DataStore

    App->>Cache: 1. Read from cache
    Cache->>DataStore: 2. Read from data store, if not in cache
    DataStore-->>Cache: Data
    Cache->>Cache: 3. Store in cache
    Cache-->>App: 4. Return to app
```

#### Refresh-ahead

```mermaid
sequenceDiagram
    participant App
    participant Cache
    participant DataStore

    App->>Cache: 1. Read from cache
    Cache-->>App: Return stale data
    Cache->>DataStore: 2. Read from data store (asynchronously)
    DataStore-->>Cache: Fresher data
    Cache->>Cache: Update cache
```

### Write-intensive application caching strategies

#### Write-through

```mermaid
sequenceDiagram
    participant App
    participant Cache
    participant DataStore

    App->>Cache: 1. Write to cache
    Cache->>DataStore: 2. Write to data store
    DataStore-->>Cache: Ack
    Cache-->>App: Ack
```

#### Write-around

```mermaid
sequenceDiagram
    participant App
    participant DataStore
    participant Cache

    App->>DataStore: 1. Write to data store
    DataStore-->>Cache: 2. Async write to cache
    DataStore-->>App: Ack
```

#### Write-back

```mermaid
sequenceDiagram
    participant App
    participant Cache
    participant DataStore

    App->>Cache: 1. Multiple writes to cache
    Cache-->>App: Ack
    Cache-->>DataStore: 2. Async write to data store
```
