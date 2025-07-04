﻿# 🚀 MCP Server – FastAPI + Claude AI ( On going )
 

A lightweight, Claude-compatible **MCP (Multi-Call Plugin) Server** built using FastAPI. Exposes tools and REST endpoints for seamless integration with Claude AI.

---

## 📦 Features

- ⚡ FastAPI-based backend
- 🔌 MCP-compliant `/mcp` endpoint
- 🐳 Docker-ready setup
- 🧪 Swagger UI for testing

---

## 🐳 Quick Start (Docker)

```bash
# Clone repo
git clone https://github.com/yourusername/mcp-server.git
cd mcp-server

# Build image
docker build -t mcp-demo .

# Run container
docker run -p 8000:8000 mcp-demo
