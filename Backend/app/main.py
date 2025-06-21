from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mcp import FastApiMCP

from .routers import health, users
from . import tools  # the module, not an MCP instance

# 1) normal FastAPI app
app = FastAPI(title="FastAPI + MCP demo")

# 2) REST routers
app.include_router(health.router)
app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3) MCP server – pass `app` into the constructor (new requirement in v0.3+)
mcp = FastApiMCP(
    app,
    name="My-API-MCP",
    include_operations=["*"],          # expose all FastAPI routes
    describe_full_response_schema=True
)

# 4) register any *extra* tools that are not FastAPI routes
tools.register_tools(mcp)

# 5) finalise internal schema
mcp.mount()

# ---- optional CLI runner for local dev ----
def run():
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
