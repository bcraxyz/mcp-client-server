from fastmcp import FastMCP

mcp_server = FastMCP("MCP Server Demo 🚀")

@mcp_server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp_server.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp_server.run(transport="sse", host="0.0.0.0", port=8000)
