---
title: "Design Strategy"
date: 2025-10-24
type: diagram
tags:
  - design
  - compound-interest
---

### Two Paths of Product Design

```mermaid
graph TD
    subgraph "The Wrong Way:<br/>Planting Shrubs"
        direction TB
        A1("Start: 'Innovate' Quickly") --> A2("Plant 20+ Features");
        A2 --> A3("Hope One Sticks");
        A3 --> A4("Result: Feature Bloat & User Confusion");
        A4 --> A5("Outcome: Short-term thinking, product fails or stagnates");
    end

    subgraph "The Smart Way:<br/>Planting the Tree"
        direction TB
        B1("Start: Identify a Core Problem") --> B2("Plant a Single 'Tree': Solve the problem exceptionally well");
        B2 --> B3("Apply Craft, Patience & Restraint");
        B3 --> B4("Let Time & User Behavior Do the Work");
        B4 --> B5("Outcome: Compound Interest - Loyalty, Value, and Natural Growth");
    end

    style A4 fill:#ffcccc,stroke:#333,stroke-width:2px
    style B4 fill:#cce5ff,stroke:#333,stroke-width:2px
    style A5 fill:#ff9999,stroke:#333,stroke-width:2px
    style B5 fill:#99ccff,stroke:#333,stroke-width:2px
```

### The Core Principles of Compound Interest Design

```mermaid
mindmap
  root((Compound Interest <br/> of Design))
    ::icon(fa fa-seedling)
    <b>Core Principle: "Plant the Tree"</b>
      ::icon(fa fa-tree)
      Solve ONE core problem perfectly
      Invest in foundational details & craft
      Exercise restraint (what NOT to build)
    <b>The Wrong Way: "Plant Shrubs"</b>
      ::icon(fa fa-leaf)
      Feature bloat dressed as innovation
      Chasing trends
      Impatience & short-term focus
    <b>Positive Outcomes</b>
      ::icon(fa fa-arrow-trend-up)
      User Retention & Habit Formation
      Delight & Brand Personality
      Long-term Value & Growth
    <b>Examples</b>
      ::icon(fa fa-lightbulb)
      Shopify's Shop App
        (Started with just package tracking)
      Duolingo's Micro-interactions
        (Delight in pull-to-refresh)
      Slice App
        (Laser-focus on pizza)
```

### Evolution of a Well-Planted "Tree" (Shopify Example)

```mermaid
sequenceDiagram
    title: Shopify's "Plant the Tree" Evolution
    participant User
    participant Shop App

    Note over User, Shop App: The "Tree": Solve one problem perfectly
    User->>Shop App: Where is my package? (Core need)
    Shop App-->>User: Delivers an exceptional package tracking experience.

    Note over User, Shop App: Time Passes: User trust and habit forms...

    Note over User, Shop App: A "Branch" Grows Naturally
    Shop App->>User: Introduces the "Shop Button" at checkout.
    User-->>Shop App: Adopts the new feature because the core app is trusted.

    Note over User, Shop App: More "Branches" Grow from a Strong Foundation
    Shop App->>User: Adds personalized recommendations & a full marketplace.
    User-->>Shop App: Engages deeper, trusting the platform's evolution.
```

Sources:

- [The compound interest of design: what not to build](https://designobserver.com/the-compound-interest-of-design-what-not-to-build/)
