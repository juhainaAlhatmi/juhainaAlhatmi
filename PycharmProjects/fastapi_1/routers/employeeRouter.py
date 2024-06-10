

from fastapi import APIRouter
from models.employee_models import *


employeeRouter = APIRouter()



@employeeRouter.get("/hellowEmployee")
async def hellowE():
    return "hi employee"

@employeeRouter.get('/TeamId')
async def read_root():
    return "Team_Id"

@employeeRouter.get('/NameOfTeam')
async def read_root():
    return "NameOfTeam"

@employeeRouter.get('/AdminOfTeam')
async def read_root():
    return "AdminOfTeam"

@employeeRouter.get('/Employee_id')
async def read_root():
    return "Employee_id"

@employeeRouter.get('/PhoneNumber')
async def read_root():
    return "PhoneNumber"

@employeeRouter.get('/Collage')
async def read_root():
    return "Collage"

@employeeRouter.get('/Email')
async def read_root():
    return "Email"


@employeeRouter.get('/Budget_id')
async def read_root():
    return "Budget_id"

@employeeRouter.get('/Budget_Date')
async def read_root():
    return "Budget_Date"


@employeeRouter.get('/Budget_Year')
async def read_root():
    return "Budget_Year"

@employeeRouter.get('/BudgetDate_Use')
async def read_root():
    return "BudgetDate_Use"

@employeeRouter.get('/BudgetCost_Use')
async def read_root():
    return "BudgetCost_Use"


#post



@employeeRouter.post("/goal")
async def create_goal(goal : Goal):
    return {" GoalsOfTeam :": goal}

# @employeeRouter.post("/event")
# async def create_event(event : Event):
#     return "done!"

@employeeRouter.post("/eventd")
async def create_event(eventd :EventD):
    return {"Event_Date : ":eventd}

@employeeRouter.post("/time")
async def create_time(time :Time):
    return {"The Event Time will be :":time }

@employeeRouter.post("/palce")
async def create_place(place :Place):
    return {"we want event in the place":place}

@employeeRouter.post("/goalse")
async def create_goalse(goalse:GoalsE):
    return {"for this Event we have mane Goals are : ": goalse}

@employeeRouter.post("/expected")
async def create_expected(expected :Expected):
    return {"the price we expected is : ": expected}


@employeeRouter.post("/need")
async def create_neede(need :Need):
    return {"The all thing we needs for the event are : " : need}

@employeeRouter.post("/summary")
async def create_summary(saummary :Summary):
    return {"Summary of Event is : ":saummary}

@employeeRouter.post("/organizer")
async def create_organizer( organizer:Organizer):
    return {"The name for organizers :": organizer}

@employeeRouter.post("/partcipant")
async def create_partcipant(partcipant : Partcipant):
    return {" The Name Of Partcipant : ":partcipant}

@employeeRouter.post("/sponsor")
async def create_sponsor(sponsor : Sponsor):
    return {"the sponsor for this event : ": sponsor}

@employeeRouter.post("/level")
async def create_level(level : Level):
    return {"Type of level for Event : ": level}

@employeeRouter.post("/type")
async def create_type(type : Type):
    return {"Type of Event : ": type}

@employeeRouter.post("/room")
async def create_room(room : Room):
    return {"The Room you want for event : ":room}

@employeeRouter.post("/cost")
async def create_cost(cost : Cost):
    return {"The Cost of Event : ": cost}


@employeeRouter.post("/internal")
async def create_internal(internal: Internal):
    return {"The internal cost is : ":internal}

@employeeRouter.post("/external")
async def create_external(external : External):
    return {"The external cost is : ":external}

@employeeRouter.post("/expenses")
async def create_expenses(expenses : Expenses):
    return {"the event expensive : ": expenses}

@employeeRouter.post("/add")
async def create_add(add : Add):
    return {"the price add latter is : ": add}

@employeeRouter.post("/remaining")
async def create_remaining(remaining : Remaining):
    return {"the price remaining : ":remaining}

@employeeRouter.post("/joint")
async def create_joint(joint : JoinT):
    return{"date join to team :": joint}

@employeeRouter.post("/infoEvent")
async def create_infoEvent(infoEvent: InfoEvent):
    return {"Information of event : ": infoEvent}

@employeeRouter.post("/booking")
async def create_booking(booking : Booking):
    return {"the detail of booking : ":booking}

@employeeRouter.post("/exchange")
async def create_exchange(exchange : Exchange):
    return {"exchange of event is : ": exchange}

@employeeRouter.post("/eventD")
async def eventD(eventD : EventDetails):
    return {"All Details :":eventD}

@employeeRouter.post("/costN")
async def create_costN(costN: CostEvent):
    return {"Cost event :":costN}

@employeeRouter.post("/budgetinf")
async def create_budgetinfo(budgetinfo: BudgetInfo):
    return {"information of budget : ": budgetinfo}

