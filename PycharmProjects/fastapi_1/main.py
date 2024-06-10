
from fastapi import FastAPI
from PycharmProjects.fastapi_1.routers.employeeRouter import employeeRouter

app = FastAPI()


app.include_router(router=employeeRouter, prefix="/employee", tags=["Employee APIs"])


#app.include_router(router= studentsRouter, prefix="/student",tags=["Students APIs"])







# @app.get('/')
# async def read_root():
#     return "Hello World"
#
# @app.get('/TeamId')
# async def read_root():
#     return "Team_Id"
#
# @app.get('/NameOfTeam')
# async def read_root():
#     return "NameOfTeam"
#
# @app.get('/AdminOfTeam')
# async def read_root():
#     return "AdminOfTeam"
#
# @app.get('/Employee_id')
# async def read_root():
#     return "Employee_id"
#
# @app.get('/Student_id')
# async def read_root():
#     return "Student_id"
#
# @app.get('/PhoneNumber')
# async def read_root():
#     return "PhoneNumber"
#
# @app.get('/Collage')
# async def read_root():
#     return "Collage"
#
# @app.get('/Email')
# async def read_root():
#     return "Email"
#
# @app.get('/Budget_id')
# async def read_root():
#     return "Budget_id"
#
# @app.get('/Budget_Date')
# async def read_root():
#     return "Budget_Date"
#
#
# @app.get('/Budget_Year')
# async def read_root():
#     return "Budget_Year"
#
# @app.get('/BudgetDate_Use')
# async def read_root():
#     return "BudgetDate_Use"
#
# @app.get('/BudgetCost_Use')
# async def read_root():
#     return "BudgetCost_Use"
#
#
# @app.get('/all')
# async def read_root():
#     connection_string = (
#     'DRIVER={ODBC Driver 17 for SQL Server};'
#     'Server=DEVELOPERTEST01;'
#     'Database=tempdb;'
#     'UID=trainee;'
#     'PWD=train@2024;'
#     )
#     try:
#         cnxn = pyodbc.connect(connection_string)
#         print("connection successful!")
#     except pyodbc.DatabaseError as e:
#         print(f"Connection failed : {e}")
#     return {"message":"Hello world"}
#
#
#
#
# @app.post("/item")
# async def create_item(item : Item):
#     return "done!"
#
#
#
# @app.post("/goal")
# async def create_goal(goal : Goal):
#     return "done!"
#
#
#
#
#
# @app.post("/event")
# async def create_event(event :Event):
#     return "done!"
#
#
#
#
# @app.post("/eventd")
# async def create_event(eventd :EventD):
#     return "done!"
#
#
#
#
# @app.post("/time")
# async def create_time(time :Time):
#     return "done!"
#
#
#
#
# @app.post("/palce")
# async def create_place(place :Place):
#     return "done!"
#
#
#
#
#
# @app.post("/goalse")
# async def create_goalse(goalse:GoalsE):
#     return "done!"
#
#
#
#
#
# @app.post("/expected")
# async def create_expected(expected :Expected):
#     return "done!"
#
#
#
# @app.post("/need")
# async def create_neede(need :Need):
#     return "done!"
#
#
#
#
# @app.post("/summary")
# async def create_summary(saummary :Summary):
#     return "done!"
#
#
#
#
# @app.post("/organizer")
# async def create_organizer( organizer:Organizer):
#     return "done!"
#
#
#
#
# @app.post("/partcipant")
# async def create_partcipant(partcipant : Partcipant):
#     return "done!"
#
#
#
#
#
# @app.post("/sponsor")
# async def create_sponsor(sponsor : Sponsor):
#     return "done!"
#
#
#
#
# @app.post("/level")
# async def create_level(level : Level):
#     return "done!"
#
#
#
#
# @app.post("/type")
# async def create_type(type : Type):
#     return "done!"
#
#
#
#
# @app.post("/room")
# async def create_room(room : Room):
#     return "done!"
#
#
#
#
# @app.post("/cost")
# async def create_cost(cost : Cost):
#     return "done!"
#
#
#
#
#
# @app.post("/internal")
# async def create_internal(internal: Internal):
#     return "done!"
#
#
#
# @app.post("/external")
# async def create_external(external : External):
#     return "done!"
#
#
#
#
# @app.post("/expenses")
# async def create_expenses(expenses : Expenses):
#     return "done!"
#
#
#
#
# @app.post("/add")
# async def create_add(add : Add):
#     return "done!"
#
#
#
#
# @app.post("/remaining")
# async def create_remaining(remaining : Remaining):
#     return "done!"
#
#
#
#
# @app.post("/team")
# async def create_team(team :Team):
#     cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'
#                           'Server=Developertest01;'
#                           'Database=tempdb;'
#                           'User ID=trainee;'
#                           'Password=Train@2024')
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT * FROM Team")
#     row = cursor.fetchone()
#     while row:
#         print(row)
#         row = cursor.fetchone()
#     cursor.close()
#     cnxn.close()
#     return "done!"
#
#
#
#
#
# @app.post("/joint")
# async def create_joint(joint : JoinT):
#     return "done!"
#
#
#
#
#
# @app.post("/infoEvent")
# async def create_infoEvent(infoEvent: InfoEvent):
#     return "done!"
#
#
#
#
# @app.post("/booking")
# async def create_booking(booking : Booking):
#     return "done!"
#
#
#
#
#
# @app.post("/exchange")
# async def create_exchange(exchange : Exchange):
#     return "done!"
#
#
#
#
# @app.post("/eventD")
# async def create_eventD(eventD : EventDetails):
#     return "done!"
#
#
#
#
# @app.post("/costN")
# async def create_costN(costN: CostEvent):
#     return "done!"
#
#
#
#
#
# @app.post("/budgetinf")
# async def create_Budgetinfo(budgetinfo: BudgetInfo):
#     return "done!"
#
#
# @app.get("/Team/{Team_id}")
#
# def read_item(Team_id: int= None):
#
#     return {"Team_id": Team_id}
#
#
#
