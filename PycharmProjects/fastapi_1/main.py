
from fastapi import FastAPI
from routers.employeeRouter import employeeRouter
from routers.studentRouter import studentsRouter

app = FastAPI()


app.include_router(router=employeeRouter, prefix="/employee", tags=["Employee APIs"])


app.include_router(router= studentsRouter, prefix="/student",tags=["Students APIs"])







# @app.get('/')
# async def read_root():
#     return "Hello World"
#

#

#


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
#
# @app.get("/Team/{Team_id}")
#
# def read_item(Team_id: int= None):
#
#     return {"Team_id": Team_id}
#
#
#
