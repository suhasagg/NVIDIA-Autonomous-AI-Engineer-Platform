from fastapi import APIRouter,Depends
from app.security import auth
from app.domain import GoalRequest,Plan
from app.skills import list_skills
from app.service import Service
from app.runtime import Runtime
router=APIRouter(prefix="/v1",dependencies=[Depends(auth)])
@router.get("/skills")
async def skills():return {"skills":list_skills()}
@router.post("/goals")
async def goals(r:GoalRequest):return await Service().goal(r)
@router.post("/plans/execute")
async def plans(p:Plan):return {"outputs":await Runtime().execute(p)}
