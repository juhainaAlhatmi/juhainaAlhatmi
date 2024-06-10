from datetime import datetime

from fastapi import APIRouter

employeeRouter = APIRouter()



@employeeRouter.get("/hellowEmployee")
async def hellowE():
    return "hi employee"


