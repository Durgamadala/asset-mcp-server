from server import mcp
import uvicorn
import os

# MCP app
app = mcp.streamable_http_app()

# 🚨 IMPORTANT FIX: disable host blocking
try:
    from fastapi.middleware.trustedhost import TrustedHostMiddleware

    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=["*"]
    )
except Exception:
    pass  # in case fastapi middleware isn't used in your MCP build

print("MCP server initialized")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        proxy_headers=True,
        forwarded_allow_ips="*"
    )
