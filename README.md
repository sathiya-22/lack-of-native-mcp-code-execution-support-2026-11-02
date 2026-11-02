# MCP Executor for LangChain (Proof of Concept)

## The Real Problem and Who It Affects

The Model Context Protocol (MCP) aims to standardize how AI models interact with external tools and services, enabling more robust and composable agentic systems. A key aspect of MCP is programmatic tool calling and lazy result loading, where the agent decides *when* and *how* to execute a tool, and only fetches results when needed.

LangChain, a popular framework for developing LLM applications, currently lacks native, first-class support for MCP-style code execution. Developers often resort to implementing custom `BaseTool` wrappers or convoluted callback mechanisms to simulate programmatic execution and lazy loading. This increases development complexity, reduces code clarity, and makes it harder to integrate with existing or future MCP-compliant services.

This prototype addresses this by providing a conceptual framework and a minimal implementation for an MCP-compatible tool execution environment that can be integrated with LangChain. It focuses on demonstrating programmatic execution and lazy result fetching without requiring extensive workarounds.

## Why This Project Shape/Stack Was Chosen

This project is a Python package because LangChain itself is primarily Python-based, making direct integration most straightforward. The chosen shape provides:
-   **Clear API:** A `MCPToolExecutor` class that can manage and execute MCP-like tool definitions.
-   **LangChain Compatibility:** Demonstrates how such an executor could integrate with LangChain's `BaseTool` interface, allowing existing agents to leverage it.
-   **Self-Contained:** Uses a simple in-memory "tool registry" and mock execution to prove the concept without external dependencies.
-   **Focus on Protocol:** The core logic focuses on the *execution protocol* rather than the LLM's reasoning, making it provider-agnostic.

## Setup and Usage Instructions (Zero API Keys)

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the example:**
    The `main.py` script demonstrates the core functionality. It defines a mock MCP tool, registers it, and then simulates an agent requesting its execution and lazily fetching results.

    ```bash
    python main.py
    ```

    You will see output demonstrating:
    -   The `MCPToolExecutor` receiving a tool call.
    -   The tool's execution being "queued" (represented by a future/promise).
    -   The ability to retrieve the result later, simulating lazy loading.
    -   How this can be wrapped into a LangChain `BaseTool`.

## Optional Real-LLM Adapter

This prototype does *not* include an optional real-LLM adapter. The problem it addresses is specifically about the *execution infrastructure* for tools, not the LLM's ability to *call* them. The LLM's role is to output a tool call (e.g., in JSON), which this system would then parse and execute. The core logic here is LLM-agnostic, focusing solely on the execution layer.
