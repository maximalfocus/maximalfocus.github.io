---
title: "Playwright"
date: 2025-10-08
type: diagram
tags:
  - playwright
  - selenium
  - cypress
---

### Playwright's Core Architecture

```mermaid
graph TD
    TestScript[Test Script - <br> Python/JS/Java/.NET] -- JSON over WebSocket --> PlaywrightServer{Playwright Server};
    PlaywrightServer -- Results --> TestScript;
    
    PlaywrightServer -- DevTools Protocol --> Browser["Browser <br> (Chromium, Firefox, WebKit)"];
    Browser -- Events --> PlaywrightServer;
```

### Architectural Comparison: Playwright vs. Selenium vs. Cypress

```mermaid
graph TD

    subgraph Cypress
        direction TB
        C1[Node.js Test Runner] --> |In-Process| C2[Browser];
        C2 --> |Runs tests and app in the same event loop| C1;
    end

    subgraph Selenium
        direction TB
        S1[Test Script] --> |HTTP JSONWire/W3C| S2[Browser Driver];
        S2 --> |Browser-specific Protocol| S3[Browser];
    end

    subgraph Playwright
        direction TB
        P1[Test Script] --> |WebSocket| P2[Playwright Server];
        P2 --> |DevTools Protocol| P3[Browser];
    end
```

### Playwright's Browser Context Isolation

```mermaid
graph TD
    Script(Playwright Script) --> BrowserInstance(Browser Instance);
    
    BrowserInstance --> Context1("Browser Context 1 <br> (Isolated Cookies, Storage)");
    BrowserInstance --> Context2("Browser Context 2 <br> (Isolated Cookies, Storage)");
    
    Context1 --> Page1(Page 1);
    Context1 --> Page2(Page 2);
    
    Context2 --> Page3(Page 3);
```

### Playwright's Locator Auto-Waiting Mechanism

```mermaid
graph TD
    Trigger["Action Triggered on Locator <br> e.g., button.click()"] --> Check{"Is element actionable? <br> (visible, enabled, etc.)"};
    
    Check -- Yes --> PerformAction(Perform Action);
    PerformAction --> Success(Action Succeeded);
    
    Check -- No --> Wait{Wait for Actionability};
    Wait -- Becomes Actionable --> Check;
    Wait -- Timeout --> Error(Throw Timeout Error);
```

### Playwright's Network Interception

```mermaid
sequenceDiagram
    participant TestScript
    participant Playwright
    participant Browser
    participant Server

    TestScript->>Playwright: page.route('**/api/data', ...)
    
    Browser->>Playwright: Request /api/data
    activate Playwright
    Note over Playwright,Server: Request is intercepted and does not reach the Server
    
    Playwright->>TestScript: Invoke route handler
    activate TestScript
    
    TestScript-->>Playwright: Return Mock Response
    deactivate TestScript
    
    Playwright-->>Browser: Fulfill request with Mock Response
    deactivate Playwright
```
