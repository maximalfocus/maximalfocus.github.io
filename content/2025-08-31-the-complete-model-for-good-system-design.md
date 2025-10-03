---
title: "The Complete Model for Good System Design"
date: 2025-08-31
type: post
tags:
  - system-design
  - good-design
---

### The Complete Model for Good System Design

This document presents a comprehensive blueprint for designing and building robust, scalable, and secure systems. It is built upon a foundation of core principles, a layered architectural model, and non-negotiable standards that apply system-wide.

---

### 1. Guiding Principles: The Architectural North Star

Every design decision must be measured against these foundational principles. They are the constitution of the architecture.

*   **Principle of Least Complexity:** The best design is the simplest one that correctly solves the problem. We do not add technology or components for their own sake. Complexity is a liability that must be rigorously justified, as a system that is easy to understand is easy to maintain, operate, and extend.
*   **Principle of Predictable Simplicity:** Favor boring, well-understood technologies. A system built on proven components (e.g., PostgreSQL, Redis, Kafka) will be more reliable and easier to operate than one built on novel or niche technologies. Good design should be effective, not "impressive."
*   **Principle of State Encapsulation:** State is the primary source of complexity and failure. Its management must be deliberate and contained. State will not be scattered; it will be owned and protected within clear service boundaries.
*   **Principle of Security by Design:** Security is a foundational requirement, not a feature. Every component and data flow must be designed with a "zero trust" mindset. We must secure data in transit and at rest, manage secrets rigorously, and implement the principle of least privilege for all interactions.
*   **Principle of Designed Resilience:** The system must assume failure as a normal operating condition. Every component and interaction must be designed with a clear understanding of what happens when dependencies fail. The system's default state is to remain functional, even if in a degraded capacity.
*   **Principle of Evolutionary Architecture:** A complex system that works is always an evolution of a simple system that worked. We will not design a complex, end-state system from day one. The architecture must be designed to grow and adapt incrementally.

---

### 2. The Model Architecture: A Layered Blueprint

This model is a container-based, Service-Oriented Architecture (SOA) organized into distinct layers, moving from the external entry point to the core data stores.

#### Layer 1: The API Gateway Layer

This is the single, managed entry point for all external client requests. It acts as a protective and simplifying facade for the internal system.

*   **Purpose:** To abstract and secure the internal service landscape.
*   **Responsibilities:**
    *   **Request Routing:** Directs incoming traffic to the appropriate internal service.
    *   **Authentication & Authorization:** Enforces who can access the system and what they are allowed to do before a request reaches an internal service.
    *   **Rate Limiting & Throttling:** Protects the system from abuse and overload.
    *   **SSL Termination:** Offloads encryption/decryption from internal services.
    *   **Request/Response Transformation:** Adapts payloads for different client needs.

#### Layer 2: The Service Layer

This is the home of all business logic, decomposed into two distinct service types.

*   **Stateless Services:**
    *   **Purpose:** To perform computation, execute logic, and transform data.
    *   **Rules:** They MUST NOT persist state between requests. They are scaled horizontally to handle load, and their failure is non-critical, as a new instance can immediately replace a failed one.
*   **Stateful Services (Gatekeepers):**
    *   **Purpose:** To own and manage a specific domain of the system's state.
    *   **Rules:** This service is the sole authority for its data. Any other service that needs to read or modify this state MUST do so via this service's well-defined API. Direct database access from other services is strictly forbidden.

#### Layer 3: The Purpose-Fit Persistence Layer

This layer is the foundation of the system's state, using the right storage technology for the right job.

*   **Primary Database (Relational - e.g., PostgreSQL):** The source of truth for core, structured business data. All read traffic that can tolerate minimal replication lag MUST be directed to read-replicas.
*   **Caching Layer (In-Memory - e.g., Redis):** A high-speed, ephemeral store to reduce latency. The system MUST function correctly if the cache is lost. Caching is a performance optimization, not a fix for a poor data model.
*   **Object Storage (e.g., S3, Azure Blob Storage):** The definitive home for unstructured data and large binary objects (user files, reports, backups). It is the standard for anything that is not structured, relational data.

#### Layer 4: The Asynchronous Processing Layer

This layer enables the system to perform slow or non-critical tasks without blocking user-facing interactions.

*   **Background Job Queues:** For offloading long-running or deferrable tasks (e.g., sending emails, processing files). Jobs MUST be designed to be idempotent and retryable.
*   **Event Bus (e.g., Kafka):** For decoupled, "fire-and-forget" communication. Use when a service needs to broadcast that "something happened" without knowing or caring about the consumers. For direct, command-like interactions, a synchronous API call is preferred.

---

### 3. Cross-Cutting Concerns: System-Wide Mandates

These standards apply horizontally to every component and layer in the architecture.

*   **Comprehensive Observability:**
    *   **Logging:** Logs must be structured (JSON). Log aggressively on unhappy paths with sufficient context for debugging.
    *   **Metrics:** Every service must expose key operational metrics (latency, error rate, saturation). Track performance percentiles (p95, p99), not just averages.
    *   **Tracing:** Requests spanning multiple services must have a correlation ID to allow for distributed tracing.
*   **Rigorous Fault Tolerance:**
    *   **Idempotency:** All write APIs (POST, PUT, PATCH) must support idempotency keys to allow for safe client retries.
    *   **Circuit Breakers:** All critical inter-service communication must be wrapped in a circuit breaker to prevent cascading failures.
    *   **Conscious Failure Modes:** For every dependency, a documented decision of "fail open" or "fail closed" must be made and implemented.
*   **Pervasive Security:**
    *   **Identity and Access Management (IAM):** All service-to-service and user-to-service communication must be authenticated and authorized.
    *   **Secret Management:** Secrets (passwords, API keys) must be injected at runtime from a secure vault, not stored in code or configuration files.
    *   **Data Encryption:** All data must be encrypted in transit (TLS) and at rest.
*   **Externalized Configuration:**
    *   Application configuration (e.g., database URLs, feature flags) must be externalized from the code and supplied via the environment. This allows a single build artifact to be promoted across all environments (dev, staging, prod) without code changes.

---

### 4. The Operational Foundation: How It Runs

The architectural design is realized through a modern, automated operational environment.

*   **Containerization and Orchestration:** All services MUST be packaged as containers (e.g., Docker) and deployed on a container orchestration platform (e.g., Kubernetes). This provides consistency, scalability, and self-healing.
*   **Infrastructure as Code (IaC):** All underlying infrastructure (networks, databases, clusters) MUST be defined as code (e.g., Terraform). This ensures repeatable, auditable, and reliable environments.
*   **CI/CD Automation:** The path from code commit to production deployment MUST be fully automated through a CI/CD pipeline, incorporating automated testing, security scanning, and deployment strategies.

---

### 5. Put Theory Into Practice

* [Design Connect Chat](https://github.com/zhu-weijie/design-connect-chat)
* [Design FinCore Payments](https://github.com/zhu-weijie/design-fincore-payments)
* [AI-Powered Guardian](https://github.com/zhu-weijie/ai-powered-guardian)
* [Design Axon AI Serving](https://github.com/zhu-weijie/design-axon-ai-serving)
* [Design Classify Hub](https://github.com/zhu-weijie/design-classify-hub)
* [Design YouTube System](https://github.com/zhu-weijie/design-youtube-system)
* [Design InkWell Platform](https://github.com/zhu-weijie/design-inkwell-platform)
* [Design Patient Notification System](https://github.com/zhu-weijie/design-patient-notification-system)
* [Design Medical Claims System](https://github.com/zhu-weijie/design-medclaim-assure)
* [Design Pulse Analytics](https://github.com/zhu-weijie/design-pulse-analytics)
