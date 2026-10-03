class EngineeringMemory:
 def __init__(self):self.working={};self.session={};self.episodic={};self.semantic={};self.entity={};self.procedural={}
 def put(self,l,k,v):getattr(self,l)[k]=v
 def get(self,l,k,d=None):return getattr(self,l).get(k,d)
