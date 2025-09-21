---
title: "Docker Lifecycle"
date: 2025-09-07
type: diagram
tags:
  - docker
  - lifecycle
---

```mermaid
stateDiagram-v2
    [*] --> Created: Create
    [*] --> Running: Run
    Created --> Running: Start
    Running --> Paused: Pause
    Paused --> Running: Unpause
    Running --> Stopped: Stop
    Stopped --> Running: Restart
    Stopped --> Deleted: rm
    Created --> Deleted: rm
```
