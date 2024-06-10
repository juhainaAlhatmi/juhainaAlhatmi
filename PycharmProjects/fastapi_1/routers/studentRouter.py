from fastapi import APIRouter
studentsRouter = APIRouter()


@studentsRouter.get('/Student_id')
async def read_root():
    return "Student_id"



@studentsRouter.get('/PhoneNumber')
async def read_root():
    return "PhoneNumber"

@studentsRouter.get('/Collage')
async def read_root():
    return "Collage"

@studentsRouter.get('/Email')
async def read_root():
    return "Email"