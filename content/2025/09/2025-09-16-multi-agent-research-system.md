---
title: "Multi-Agent Research System"
date: 2025-09-16
type: diagram
tags:
  - multi-agent
  - research-system
  - ai
---

### Multi-Agent Research System

```mermaid
graph LR
    subgraph "Multi-agent research system"
        direction LR
        
        subgraph " "
          direction LR
          Citations["Citations<br/>subagent"]
          subgraph "Search subagents"
              direction TB
              Search1["Search subagent"]
              Search2["Search subagent"]
              Search3["Search subagent"]
          end
        end

        subgraph " "
            direction LR
            LeadAgent["<b>Lead agent<br/>(orchestrator)</b><br/><br/>Tools: search tools + MCP tools<br/>+ memory + run_subagent +<br/>complete_task"]
            Memory["Memory"]
        end
        
    end

    subgraph "Claude.ai chat"
        UserChat("<b>What's on your mind tonight?</b><br/><br/>what are all the companies in the<br/>united states working on AI agents in 2025?<br/>make a list of at least 100. for each<br/>company, include the name, website,<br/>product, description of what they do,<br/>type of agents they build, and their<br/>vertical/industry.")
    end

    %% Connections
    UserChat -- "User request" --> LeadAgent
    LeadAgent -- "Final report" --> UserChat
    LeadAgent --> Citations
    LeadAgent --> Memory
    LeadAgent --> Search1
    LeadAgent --> Search2
    LeadAgent --> Search3

    Search1 --> Search1
    Search2 --> Search2
    Search3 --> Search3
    
    %% Styling
    style Citations fill:#333,stroke:#666,stroke-width:2px,color:#fff
    style LeadAgent fill:#333,stroke:#666,stroke-width:2px,color:#fff
    style Memory fill:#333,stroke:#666,stroke-width:2px,color:#fff
    style Search1 fill:#333,stroke:#666,stroke-width:2px,color:#fff
    style Search2 fill:#333,stroke:#666,stroke-width:2px,color:#fff
    style Search3 fill:#333,stroke:#666,stroke-width:2px,color:#fff
    style UserChat fill:#333,stroke:#666,stroke-width:2px,color:#fff
```

### Multi-Agent System Process Diagram

```mermaid
%%{init: {'theme': 'dark'}}%%
sequenceDiagram
    participant User
    participant System
    participant LeadResearcher
    participant Subagent1
    participant Subagent2
    participant Memory
    participant CitationAgent

    User->>System: send user query
    System->>LeadResearcher: Create Lead Researcher

    loop Iterative Research Process
        LeadResearcher->>LeadResearcher: think (plan approach)
        LeadResearcher->>Memory: save plan
        Memory-->>LeadResearcher: retrieve context
        
        LeadResearcher->>Subagent1: create subagent for aspect A
        LeadResearcher->>Subagent2: create subagent for aspect B

        par 
            Subagent1->>Subagent1: web_search
            Subagent1->>Subagent1: think (evaluate)
            Subagent1-->>LeadResearcher: complete_task
        and 
            Subagent2->>Subagent2: web_search
            Subagent2->>Subagent2: think (evaluate)
            Subagent2-->>LeadResearcher: complete_task
        end

        LeadResearcher->>LeadResearcher: think (synthesize results)
        
        alt More research needed?
            Note over LeadResearcher: Continue loop
        else 
            Note over LeadResearcher: Exit loop
        end
    end

    LeadResearcher-->>System: complete_task (research result)
    Note over System, CitationAgent: Process documents + research report to identify locations for citations
    System->>CitationAgent: Return report with citations inserted
    System->>System: Persist results
    System-->>User: Return research results with citations
```

### The Power vs. Cost Trade-off

```mermaid
%%{init: {'theme': 'dark'}}%%
graph TB
    subgraph "The Power vs. Cost Trade-off"
        direction TB

        subgraph "Performance on Complex Queries"
            direction TB
            
            subgraph " "
                direction LR
                SingleAgent["Single-Agent System"]
                MultiAgent["Multi-Agent System"]
            end
            
            subgraph " "
                direction LR
                Result1((X))
                Result2((✓))
            end

            SingleAgent -- "Fails to find answer" --> Result1;
            MultiAgent -- "<b>+90.2% performance</b>" --> Result2;
        end

        subgraph "Relative Token Cost"
            direction LR
            A["Standard Chat<br/>(Baseline: 1x)"]
            B["Single-Agent System<br/>(Approx. 4x)"]
            C["Multi-Agent System<br/>(Approx. 15x)"]
            
            style A height:50px,fill:#87CEEB, color:#000
            style B height:80px,fill:#FFA500, color:#000
            style C height:120px,fill:#FF6347, color:#000
        end
    end

    %% Styling for nodes and links
    style SingleAgent fill:#f9f,stroke:#999,stroke-width:1px, color:#000
    style MultiAgent fill:#9f9,stroke:#999,stroke-width:1px, color:#000
    linkStyle 0 stroke:red,stroke-width:2px
    linkStyle 1 stroke:green,stroke-width:2px
```

### The AI Agent Evaluation Pyramid

```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    subgraph "Evaluation Strategy"
        A["<b>Level 1: Small-Sample Testing (Immediate)</b><br/><i>Finds major issues quickly</i><br/><br/>- Use ~20 representative queries<br/>- Catches large-impact failures<br/>- Enables rapid iteration"];
        B["<b>Level 2: LLM-as-Judge (Scaled)</b><br/><i>Grades outputs against a rubric</i><br/><br/>- Factual & citation accuracy<br/>- Completeness of the answer<br/>- Tool efficiency & source quality"];
        C["<b>Level 3: Human Evaluation</b><br/><i>Catches nuance and edge cases</i><br/><br/>- Identifies source quality bias<br/>- Finds subtle failures<br/>- Uncovers unexpected behaviors"];
        
        A --> B;
        B --> C;
    end
    
    %% Styling for dark theme
    style A fill:#90ee90,stroke:#aaa,stroke-width:1px,color:#000
    style B fill:#66CDAA,stroke:#aaa,stroke-width:1px,color:#000
    style C fill:#3CB371,stroke:#aaa,stroke-width:1px,color:#000
```

### Orchestrator Agent's Prompting Heuristics

```mermaid
%%{init: {'theme': 'dark'}}%%
graph TD
    A["1.Plan & Delegate"] --> B["2.Allocate Resources"];
    B --> C["3.Select Tools"];
    C --> D["4.Execute Search Strategy"];
    D --> E{"5.Self-Correct<br/><i>Evaluate results</i>"};
    
    E -- "No, task complete" --> F((Finish));
    E -- "Yes, refine strategy" --> C;

    %% Styling for the nodes
    style A fill:#333,stroke:#888,stroke-width:2px,color:#fff
    style B fill:#333,stroke:#888,stroke-width:2px,color:#fff
    style C fill:#333,stroke:#888,stroke-width:2px,color:#fff
    style D fill:#333,stroke:#888,stroke-width:2px,color:#fff
    style E fill:#5c3c3c,stroke:#c88,stroke-width:2px,color:#fff
    style F fill:#2a523a,stroke:#7c7,stroke-width:2px,color:#fff
```

Source: [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
