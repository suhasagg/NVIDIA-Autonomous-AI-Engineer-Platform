from app.security import action_hash
def test_hash():assert action_hash({"a":1,"b":2})==action_hash({"b":2,"a":1})
