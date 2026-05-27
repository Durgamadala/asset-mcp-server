from server import mcp
import uvicorn
import os
from fastapi.middleware.trustedhost import TrustedHostMiddleware

# ✅ Create MCP app
app = mcp.streamable_http_app()

# ✅ CRITICAL FIX: allow external Render/WATSONX host headers
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"]
)

# Optional debug (safe to keep)
print("Registered tools:")
for tool in mcp.tools:
    print("-", tool)

print("Routes:")
for route in app.routes:
    print(route.path)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        app,
        host="0.0.0.0",   # IMPORTANT
        port=port,        # IMPORTANT (Render requirement)
        proxy_headers=True,
        forwarded_allow_ips="*"
    )
