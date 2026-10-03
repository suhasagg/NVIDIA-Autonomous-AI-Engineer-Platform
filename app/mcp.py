import httpx
from app.config import settings
async def call(tool,args):
 if settings.tool_mode=="mock":return {"status":"MOCK","protocol":"MCP","tool":tool,"result":{"artifact":"candidate-pr"}}
 async with httpx.AsyncClient(timeout=30) as c:
  r=await c.post(f"{settings.mcp_gateway_url}/tools/call",json={"name":tool,"arguments":args});r.raise_for_status();return r.json()
