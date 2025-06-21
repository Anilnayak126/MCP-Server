# backend/app/tools.py
def register_tools(fastapi_mcp: "FastApiMCP"):
    @fastapi_mcp.mcp.tool()        # <= call it on .mcp
    async def echo(message: str) -> str:
        return message
