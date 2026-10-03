from app.planner import Planner
from app.runtime import Runtime
class Service:
 async def goal(self,r):
  p=Planner().plan(r.goal,r.context);o=await Runtime().execute(p)
  return {"status":"WAITING_APPROVAL" if any(v.get("status")=="WAITING_APPROVAL" for v in o.values() if isinstance(v,dict)) else "COMPLETED","plan":p.model_dump(),"outputs":o}
