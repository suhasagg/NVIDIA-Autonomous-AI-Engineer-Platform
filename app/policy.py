def decide(s):
 if s.risk=="HIGH":return "REQUIRE_APPROVAL"
 if s.kind=="sandbox" or s.risk=="COMPUTE":return "REQUIRE_SANDBOX"
 return "ALLOW"
