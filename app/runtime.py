from app.compiler import compile_plan
from app.policy import decide
from app.security import action_hash
from app.agents import AGENTS
from app.sandbox import execute as sandbox
from app.mcp import call as mcp
from app.evaluator import evaluate
class Runtime:
 async def execute(self,p,approved=None):
  approved=set(approved or []);compile_plan(p);pending={s.key:s for s in p.steps};done={}
  while pending:
   ready=[s for s in pending.values() if all(d in done for d in s.depends_on)]
   if not ready:raise RuntimeError("deadlock")
   for s in ready:
    payload=s.input|{"dependency_outputs":{d:done[d] for d in s.depends_on}}
    if s.kind=="approval":
     done[s.key]={"status":"APPROVED" if s.key in approved else "WAITING_APPROVAL","action_hash":action_hash({"capability":s.capability,"input":payload})}
    elif decide(s)=="REQUIRE_APPROVAL" and not any(done.get(d,{}).get("status")=="APPROVED" for d in s.depends_on):done[s.key]={"status":"BLOCKED","reason":"approval required"}
    elif s.kind=="sandbox":done[s.key]=await sandbox(s.capability,payload)
    elif s.kind=="mcp":done[s.key]=await mcp(s.capability,payload)
    elif s.kind=="evaluate":done[s.key]=evaluate(done)
    else:done[s.key]=await AGENTS[s.agent].run(s.capability,payload)
    del pending[s.key]
  return done
