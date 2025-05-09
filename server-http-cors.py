import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastmcp import FastMCP

app = FastAPI()
server = FastMCP("Math MCP Server")

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

@server.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers"""
    return a + b

@server.tool()
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers"""
    return a * b

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
