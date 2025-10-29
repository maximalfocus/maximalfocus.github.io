---
title: "Claude Agent Skills"
date: 2025-10-29
type: diagram
tags:
  - claude
  - agent-skills
---

### The Claude Ecosystem: A Modular "Building Block" Architecture

```mermaid
graph TD
    subgraph "The Claude Ecosystem"
        direction TB
        A["Claude (Core Intelligence/The Brain)"] -- "Directs & Uses" --> BB;

        subgraph BB [Building Blocks]
            direction TB
            B["<b>Skills</b><br/>(Instruction Manuals<br/><i>'How to do it'</i>)"];
            C["<b>MCPs/Tools</b><br/>(External Capabilities<br/><i>'What can be done'</i>)"];
        end

        BB -- "Are combined within" --> D["Project<br/>(Dedicated Workspace)"];
        D -- "Results in" --> E["Specific Ongoing Work<br/>(e.g., Q3 Marketing Campaign)"];
    end
    
    %% Styling
    style A fill:#c9c9ff,stroke:#333,stroke-width:2px
    style D fill:#e0d4ff,stroke:#333,stroke-width:2px
    style E fill:#f9f9f9,stroke:#333,stroke-width:1px
```

### What is a Claude Skill?

```mermaid
graph TD
    subgraph "What is a Claude Skill?"
        direction TB
        subgraph B [ ]
            direction TB
            B1["<b>Instructions & Workflow</b><br/>(e.g., Step-by-step process)"]
            B2["<b>Tools to Use</b><br/>(e.g., Ahrefs MCP, Notion)"]
            B3["<b>Resources & Standards</b><br/>(e.g., Brand Guidelines)"]
        end
        
        B -- "Are packaged into" --> C{"<b>Claude Skill</b><br/>(Reusable Manual)"};
        C -- "Enables" --> D["<b>Consistent & Automated<br/>Task Execution</b>"];
    end

    %% Styling to make the 'Skill' container visually distinct
    style B fill:#f0e6ff,stroke:#9673d3,stroke-width:2px,stroke-dasharray: 5 5
```

### How Skills Solve Portability Issues

```mermaid
graph LR
    subgraph "How Skills Solve Portability: Before vs. After"
        subgraph "<b>After: Skills are Portable & Reusable</b>"
            direction TB
            S["<b>Reusable Skill</b>"]
            P3["Project A"] -- "Uses" --> S;
            P4["Project B"] -- "Uses" --> S;
            P5["Any New Chat"] -- "Uses" --> S;
            style S fill:#e0ffe0,stroke:#0b0
        end

        subgraph "<b>Before: Instructions are Trapped</b>"
            direction TB
            subgraph P1 [Project A]
                I1["Instructions"]
            end
            
            P2["Project B"] -- "Cannot Access" --x P1;
            style I1 fill:#ffe0e0,stroke:#b00
        end
    end
```

### How Skills Solve Stackability Issues


```mermaid
graph LR
    subgraph "How Skills Solve Stackability: Before vs. After"
        subgraph "<b>After: Skills are Stackable Building Blocks</b>"
            direction TB
            CS["Copywriting Skill"] --> NTP2["New Task Project"];
            AS["Analysis Skill"] --> NTP2;
            NTP2 ==> CO["Combined Output"];
        end
        subgraph "<b>Before: Projects are Isolated</b>"
            direction TB
            
            subgraph P1 [Copywriting Project]
                I1["Instructions"]
            end

            subgraph P2 [Analysis Project]
                I2["Instructions"]
            end
            
            NTP["New Task Project"]
            
            NTP -- "Wants to combine, but cannot" --x P1
            NTP -- "Wants to combine, but cannot" --x P2
        end
    end
    
    %% Styling
    style P1 fill:#fde7e7,stroke:#b00
    style P2 fill:#fde7e7,stroke:#b00
    style CS fill:#e0ffe0,stroke:#0b0
    style AS fill:#e0ffe0,stroke:#0b0
```

### The Three Types of Claude Skills

```mermaid
mindmap
  root((Claude Skills))
    ::icon(fa fa-cogs)
    Official Skills
      ::icon(fa fa-check-circle)
      Built by Anthropic
      (e.g., theme-factory, skill-creator)
    Custom Skills
      ::icon(fa fa-user-edit)
      Created by You
      (e.g., branded-deck, keyword-research)
    Community-Created
      ::icon(fa fa-users)
      Shared by other users
      (Use with caution)
```
