import httpx
from app.config import settings
async def execute(cap,payload):
 if settings.tool_mode=="mock":return {"status":"SUCCEEDED","runtime":"OpenShell-compatible mock","isolation":{"network":"deny-by-default","credentials":"brokered","filesystem":"ephemeral"},"result":{"exit_code":0}}
 async with httpx.AsyncClient(timeout=120) as c:
  r=await c.post(f"{settings.openshell_gateway_url}/v1/sandboxes/execute",json={"capability":cap,"input":payload});r.raise_for_status();return r.json()
