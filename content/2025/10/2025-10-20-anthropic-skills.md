---
title: "Anthropic Skills"
date: 2025-10-20
type: diagram
tags:
  - anthropic
  - skills
  - mcp
  - ai
---

### High-Level Project Structure

```mermaid
mindmap
  root((Skills Project))
    Plugins
      marketplace.json
    Example Skills
      Creative & Design
        algorithmic-art
        canvas-design
        slack-gif-creator
      Development & Technical
        artifacts-builder
        mcp-builder
        webapp-testing
      Enterprise & Communication
        brand-guidelines
        internal-comms
        theme-factory
      Meta Skills
        skill-creator
        template-skill
    Document Skills
      docx
      pdf
      pptx
      xlsx
```

### The Anatomy of a Skill

```mermaid
graph TD
    A[Skill Folder: `my-skill/`] --> B{SKILL.md};
    B --> C[YAML Frontmatter];
    B --> D[Markdown Body];
    C --> E["name: my-skill (required)"];
    C --> F["description: '...' (required)"];
    D --> G[Instructions & Guidelines];
    A --> H((Optional Resources));
    H --> I[scripts/];
    H --> J[references/];
    H --> K[assets/];
    I --> L["Executable Code (.py, .sh)"];
    J --> M["Documentation (.md)"];
    K --> N[Templates, Images, etc.];
```

### "Skills" as a Superset of MCP

```mermaid
graph TD
    subgraph "Agent Skills Ecosystem"
        A(Skills)
        subgraph "Skill Categories"
            B[Creative & Design]
            C[Development & Technical]
            D[Enterprise & Communication]
            E[Meta Skills]
            F[Document Skills]
        end

        A --> B
        A --> C
        A --> D
        A --> E
        A --> F

        subgraph "Example Development Skills"
            C --> G[webapp-testing]
            C --> H[artifacts-builder]
            C --> I[mcp-builder]
        end
    end

    style I fill:#f9f,stroke:#333,stroke-width:2px
```

### Deep Dive into Document Skills

```mermaid
graph TD
    subgraph Document Skills Plugin
        A[document-skills] --> B[docx];
        A --> C[pdf];
        A --> D[pptx];
        A --> E[xlsx];
    end

    subgraph Key Capabilities
        B --> B1[Create, Edit, Analyze];
        B --> B2[Track Changes & Comments];
        B --> B3[OOXML Manipulation];

        C --> C1[Extract Text & Tables];
        C --> C2[Merge & Split];
        C --> C3[Form Handling];

        D --> D1[Generate & Edit Slides];
        D --> D2[Work with Layouts & Templates];
        D --> D3[Convert from HTML];

        E --> E1[Create & Edit Spreadsheets];
        E --> E2[Formulas & Data Analysis];
        E --> E3[Recalculate Formulas];
    end
```
