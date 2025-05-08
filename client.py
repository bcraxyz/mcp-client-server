import asyncio
from fastmcp import Client

async def main():
    # Connect via stdio to a local script
    async with Client("server.py") as client:
        tools = await client.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"- Name: {tool.name}")
            print(f"  Description: {tool.description}")
            print(f"  Input Schema:")
            for prop, details in tool.inputSchema.get("properties", {}).items():
                print(f"    - {prop}: {details['type']}")
            print()
        
        result = await client.call_tool("add", {"a": 5, "b": 3})
        for content in result:
            if hasattr(content, 'text'):
                print(f"Result: {content.text}")
            else:
                print(f"Received content of type {type(content)}: {content}")

if __name__ == "__main__":
    asyncio.run(main())
