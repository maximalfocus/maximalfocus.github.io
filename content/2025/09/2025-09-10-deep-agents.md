---
title: "Deep Agents Pattern"
date: 2025-09-10
type: post
tags:
  - deep-agents
  - ai
  - agents
---

You give an AI a multi-step task: "Research the top three alternatives to Stripe, summarize their key features, and draft a report comparing their fee structures."

The AI starts strong, but then it drifts. It loses the plot, forgets the original goal, or delivers a shallow answer that misses the crucial details. This is the core limitation of today's AI assistants. They are brilliant single-shot tools but struggle to manage and execute complex, long-term projects.

They're like a short-order cook who can make a perfect omelet on demand but can't plan, prep, and execute a five-course meal.

The solution isn't just a bigger language model; it's a better architectural pattern. This is the **Deep Agents Pattern**, a reusable blueprint for building AI that can move beyond simple chat and tackle meaningful, multi-step work. It solves the critical problem of **maintaining state, strategy, and focus over long-running tasks.**

#### The Four Components of the Deep Agents Pattern

This pattern abstracts a set of capabilities that allow an AI to function less like a reactive tool and more like a human expert. It's built on four key ideas:

1.  **Strategic Planning (The Blueprint):** Before acting, the agent creates a plan. By first breaking down a complex request into a checklist of smaller, manageable steps, it establishes a clear path to the goal. This plan serves as an anchor, preventing the agent from getting sidetracked and allowing it to track its progress.

2.  **A Workspace (Long-Term Memory):** The most significant limitation of LLMs is their finite context window. The Deep Agents pattern solves this by giving the agent an external workspace, like a virtual file system. Here, it can save notes, store research findings, and iteratively draft documents. This workspace acts as a reliable, long-term memory, ensuring no information is lost.

3.  **A Team of Specialists (Delegation):** A single person rarely handles every aspect of a complex project. They delegate. The Deep Agents pattern applies this principle by using a primary "orchestrator" agent that can spawn or call upon specialized sub-agents. It might delegate in-depth analysis to a `research-agent` and then pass the results to a `critique-agent` for review, ensuring each part of the task is handled by an expert.

4.  **A Constitution (Core Directives):** This is the agent's core identity, defined in a detailed system prompt. It's more than just a simple instruction; it's a constitution that governs the agent's behavior. It dictates how the agent should plan, when to use its tools, how to interact with its sub-agents, and the standards it must adhere to.

#### "The Art of Intelligence": A Reference Implementation

To explore and demonstrate this powerful pattern, I've initiated an open-source project called **"The Art of Intelligence."**

Its goal is to build a clean, clear, and well-documented reference implementation of the Deep Agents pattern using Python, FastAPI, and Docker. The project is designed to serve as a blueprint that others can learn from and build upon.

The overall plan for "The Art of Intelligence" is to construct an agent capable of:

*   **Receiving a high-level goal** from a user.

*   **Formulating a strategic plan** using its planning tool.

*   **Executing the plan step-by-step,** using its file system to manage its work.

*   **Delegating tasks** to specialized sub-agents for research and quality assurance.

*   **Delivering a final, polished result** that fulfills the original, complex request.

By focusing on this architecture, I am building a model for a new class of AI applications—ones that can function as true collaborators, capable of taking a complex goal and seeing it through to completion. This is the pattern that will unlock the next wave of AI-powered productivity.

GitHub: [https://github.com/zhu-weijie/the-art-of-intelligence](https://github.com/zhu-weijie/the-art-of-intelligence)

Sources:

- [https://github.com/langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)
