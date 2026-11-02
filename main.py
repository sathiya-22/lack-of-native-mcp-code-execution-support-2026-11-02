import asyncio
from mcp_executor import MCPToolExecutor, MCPToolWrapper, mock_search_tool, SearchArgs

async def main():
    print("--- Initializing MCP Executor ---")
    mcp_executor = MCPToolExecutor()

    # Register a mock search tool with the MCP executor
    mcp_executor.register_tool(
        name="search_internet",
        description="Searches the internet for information.",
        func=mock_search_tool,
        args_schema=SearchArgs
    )

    print("\n--- Demonstrating direct MCP tool execution (programmatic & lazy) ---")
    # Simulate an agent deciding to execute the tool
    print("Agent decides to call 'search_internet' for query 'latest AI news'.")
    search_future_1 = await mcp_executor.execute_tool(
        "search_internet", query="latest AI news"
    )
    print("Agent continues other tasks while search is in progress...")
    await asyncio.sleep(0.05) # Simulate other async work

    print("\nAgent decides to call 'search_internet' for query 'weather in London'.")
    search_future_2 = await mcp_executor.execute_tool(
        "search_internet", query="weather in London"
    )
    
    print("\nAgent now needs the result of the first search...")
    result_1 = await asyncio.wrap_future(search_future_1)
    print(f"Agent received first search result: {result_1}")

    print("\nAgent now needs the result of the second search...")
    result_2 = await asyncio.wrap_future(search_future_2)
    print(f"Agent received second search result: {result_2}")

    print("\n--- Demonstrating LangChain integration via MCPToolWrapper ---")
    # Create a LangChain tool instance that uses our MCP executor
    lc_mcp_tool = MCPToolWrapper(
        name="LangChain_MCP_Search",
        description="A search tool managed by the MCP Executor for LangChain agents.",
        executor=mcp_executor,
        mcp_tool_name="search_internet"
    )

    # Simulate a LangChain agent calling this tool
    print("LangChain agent calls LangChain_MCP_Search for 'best pizza recipes'.")
    lc_result = await lc_mcp_tool.arun(query="best pizza recipes")
    print(f"LangChain agent final output: {lc_result}")

if __name__ == "__main__":
    asyncio.run(main())
