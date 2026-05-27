from server import mcp
import uvicorn

app = mcp.streamable_http_app()

print("Routes:")
for route in app.routes:
    print(route.path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
