from pydantic import BaseModel,Field
from typing import Any,Literal
class GoalRequest(BaseModel):
 tenant_id:str="engineering";principal_id:str="engineer@example";goal:str;repository:str|None=None;context:dict[str,Any]=Field(default_factory=dict)
class StepSpec(BaseModel):
 key:str;agent:Literal["research","coding","debug","test","simulation","optimization","supervisor"]
 capability:str;kind:Literal["skill","mcp","sandbox","approval","evaluate"]="skill"
 depends_on:list[str]=Field(default_factory=list);input:dict[str,Any]=Field(default_factory=dict)
 risk:Literal["READ","COMPUTE","WRITE","HIGH"]="READ"
class Plan(BaseModel):objective:str;steps:list[StepSpec]
