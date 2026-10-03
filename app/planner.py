from app.domain import Plan,StepSpec
class Planner:
 def plan(self,g,ctx):
  return Plan(objective=g,steps=[
   StepSpec(key="research",agent="research",capability="research.code_search",input={"goal":g}),
   StepSpec(key="diagnose",agent="debug",capability="debug.root_cause",depends_on=["research"]),
   StepSpec(key="patch",agent="coding",capability="code.patch",depends_on=["diagnose"],risk="WRITE"),
   StepSpec(key="unit",agent="test",capability="test.unit",kind="sandbox",depends_on=["patch"],risk="COMPUTE"),
   StepSpec(key="profile",agent="optimization",capability="profile.cuda",kind="sandbox",depends_on=["unit"],risk="COMPUTE"),
   StepSpec(key="evaluate",agent="supervisor",capability="workflow.evaluate",kind="evaluate",depends_on=["unit","profile"]),
   StepSpec(key="approval",agent="supervisor",capability="git.pr.create",kind="approval",depends_on=["evaluate"],risk="HIGH"),
   StepSpec(key="pr",agent="coding",capability="git.pr.create",kind="mcp",depends_on=["approval"],risk="HIGH")])
