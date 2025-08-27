import asyncio, logging
from fastmcp import FastMCP

mcp = FastMCP(name="MathMCPServer")

logging.basicConfig(level=logging.INFO)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    logging.info(f"add() called with a={a} and b={b}")
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers"""
    logging.info(f"multiply() called with a={a} and b={b}")
    return a * b

async def main():
    await mcp.run_async(transport="streamable-http", path="/mcp", host="0.0.0.0", port=8000)

if __name__ == "__main__":
    asyncio.run(main())
