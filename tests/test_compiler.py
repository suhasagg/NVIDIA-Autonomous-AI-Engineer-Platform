from app.planner import Planner
from app.compiler import compile_plan
def test_dag():assert len(compile_plan(Planner().plan("fix",{})).nodes)==8
