from app.domain import StepSpec
from app.policy import decide
def test_high():assert decide(StepSpec(key="x",agent="coding",capability="git.pr.create",risk="HIGH"))=="REQUIRE_APPROVAL"
