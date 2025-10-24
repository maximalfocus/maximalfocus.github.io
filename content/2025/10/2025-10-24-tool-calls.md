---
title: "From Human Clicks to AI Tool Calls"
date: 2025-10-24
type: diagram
tags:
  - mcp
  - agents
  - ai
---

### The "Copy-Paste Hell" of Knowledge Work

```mermaid
graph TD
    subgraph The PhD Student's Workflow
        direction TB
        A[ChatGPT for Brainstorming] --> B{Copy-Paste};
        C[Semantic Scholar for Citations] --> B;
        B --> D[Google Docs for Drafts];
        D --> E{Copy-Paste};
        F[Grammarly for Editing] --> E;
        E --> D;
        G[Zotero for Reference Management] --> B;
        H[PDFs for Research] --> B;
    end
    style B fill:#ffcccc,stroke:#333,stroke-width:2px
    style E fill:#ffcccc,stroke:#333,stroke-width:2px
```

###  The Inefficiency of UI Automation

```mermaid
sequenceDiagram
    participant User
    participant Agent
    participant WebUI
    participant Service

    User->>Agent: "Find a citation"
    Agent->>WebUI: Click "Search Box"
    WebUI-->>Agent: Page reloads
    Agent->>WebUI: Type "Query"
    WebUI-->>Agent: Page reloads
    Agent->>WebUI: Click "Result"
    WebUI-->>Agent: Page reloads
    Note right of Agent: Each step adds latency!

    User->>Agent: "Find a citation" (with Tool Call)
    Agent->>Service: tool_call("find_citation", query="...")
    Service-->>Agent: Returns structured data
    Note right of Agent: Instant and efficient!
```

### Traditional APIs vs. AI-Native Services (MCP)

```mermaid
graph TD
    subgraph "AI-Native Service (MCP)"
        direction TB
        aiAgent["AI Agent"]
        discovers{"Discovers tool via its description"}
        understands["Understands parameters <br> from a clear schema"]
        calls["Calls the tool with a simple, <br> standardized format"]
        receives["Receives structured data"]
        
        aiAgent --> discovers --> understands --> calls --> receives
    end

    subgraph "Traditional API"
        direction TB
        developer["Developer"]
        reads{"Reads extensive <br> documentation"}
        writes["Writes custom code for a <br> specific endpoint"]
        handles["Handles complex <br> authentication"]
        parses["Parses unstructured <br> response"]

        developer --> reads --> writes --> handles --> parses
    end

    style aiAgent fill:#ccffcc,stroke:#333,stroke-width:2px
    style developer fill:#cceeff,stroke:#333,stroke-width:2px

    classDef processNode fill:#f2f2ff,stroke:#ccccff,stroke-width:2px,color:#333
    class discovers,understands,calls,receives,reads,writes,handles,parses processNode
```

### The Challenges for Service Vendors and AI Agents

```mermaid
graph TD
    subgraph "Service Vendor's Nightmare"
        direction TB
        A[Vendor builds a useful service] --> B{Shouts into the void};
        B --> C[Low discovery on GitHub, Reddit];
        B --> D[No feedback on how the tool is used];
        B --> E[Scaling issues with serverless platforms];
    end

    subgraph "AI Agent's Dilemma"
        direction TB
        F[Agent developer needs a tool] --> G{Faces the tool selection nightmare};
        G --> H[Discovery chaos: Which tool is best?];
        G --> I[Integration complexity: Each tool has quirks];
        G --> J[Authentication maze: Managing multiple keys];
        G --> K[Billing nightmare: Dozens of invoices];
    end
```

### Smithery's Orchestration Layer as the Solution

```mermaid
graph TD
    subgraph Vendors
        A[Service Vendor 1];
        B[Service Vendor 2];
        C[Service Vendor 3];
    end

    subgraph Agents
        D[AI Agent A];
        E[AI Agent B];
        F[AI Agent C];
    end

    subgraph Smithery Orchestration Layer
        G{Intelligent Gateway};
        G --> H[Distribution & Monetization];
        G --> I[Observability & Feedback];
        G --> J[Intelligent Routing & Failover];
        G --> K[Unified Auth & Quality Assurance];
    end

    A & B & C --> G;
    G --> D & E & F;

    linkStyle 0,1,2 stroke:#ff9999,stroke-width:2px;
    linkStyle 3,4,5 stroke:#99ccff,stroke-width:2px;
```

### The Evolution to an Agentic Economy

```mermaid
graph TD
    subgraph "Today's Landscape"
        direction TB
        A[Harvey for Legal]
        B[Jasper for Marketing]
        C[Vertical AI Apps]
    end

    subgraph "The Agentic Economy"
        direction TB
        D[General AI Agents] --> E[Marketplace of AI-Native Services];
        subgraph Specialized Backend Services
            F[Web Research Service]
            G[Data Analysis Service]
            H[Email Service]
            I[...]
        end
        E --> F & G & H & I;
    end

    A & B & C --> D;
```

Sources:

- [Tool Calls Are the New Clicks](https://smithery.ai/blog/tool-calls-are-the-new-clicks)
