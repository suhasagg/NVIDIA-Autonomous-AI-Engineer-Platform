def evaluate(o):
 f=[k for k,v in o.items() if isinstance(v,dict) and v.get("status") in {"FAILED","BLOCKED"}]
 return {"status":"SUCCEEDED","decision":"PASS" if not f else "REPAIR","failures":f}
