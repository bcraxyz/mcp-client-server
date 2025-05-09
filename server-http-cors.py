from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastmcp import FastMCP

app = FastAPI()

origins = [
    "*.workers.dev",
    "*.app.github.dev",
    "*.up.railway.app",
    "http://localhost",
    "http://localhost:8000",
    "https://playground.ai.cloudflare.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Create an MCP server from your FastAPI app
mcp = FastMCP.from_fastapi(app=app)

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers"""
    return a * b

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
