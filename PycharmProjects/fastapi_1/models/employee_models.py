from datetime import datetime

from pydantic import BaseModel


def emoployeeRouter():
    return None


class Goal(BaseModel):
    GoalsOfTeam: str = None


class EventD(BaseModel):
    Event_Date: str


class Time(BaseModel):
    Time: int


class Place(BaseModel):
    Place: str


class GoalsE(BaseModel):
    EventGoals: str


class Expected(BaseModel):
    ExpectedCost: float


class Need(BaseModel):
    NeedofEvent: str


class Summary(BaseModel):
    SymmaryOfEvent: str


class Organizer(BaseModel):
    NameOfOrganizer: str


class Partcipant(BaseModel):
    NameOfPartcipant: str


class Sponsor(BaseModel):
    SponsorName: str


class Level(BaseModel):
    LevelOfEvent: str


class Type(BaseModel):
    TypeOfEvent: str


class Room(BaseModel):
    Room: str


class Cost(BaseModel):
    TotalCost: float

class Money(BaseModel):
     InternalCost: float
     ExternalCost:float

# class Internal(BaseModel):
#     InternalSupport: float
#
#
# class External(BaseModel):
#     ExternalSupport: float
#
#
# class Expenses(BaseModel):
#     Expenses: float


class Add(BaseModel):
    AddBalance: str


class Remaining(BaseModel):
    RemainingBalance: float


class Team(BaseModel):
    name: str = None
    admin: str
    gaols: str


class JoinT(BaseModel):
    join_Date: datetime
    withdrawal: datetime


class InfoEvent(BaseModel):
    sponsorName: str = None
    LevelOfEvent: str
    TypeOfEvent: str
    Status: str


class Booking(BaseModel):
    Room: str


class Exchange(BaseModel):
    AddBalance: float
    RemainingBalance: float


class EventDetails(BaseModel):
    Evenetname: str = None
    Time: datetime
    place: str
    GoalsOfEvent: str
    ExpectedCost: float
    FocusOfEvent: str
    SummaryOfEvent: str
    Needs: str
    NameOfOrganizer: str
    NumberOfParticpate: int


class CostEvent(BaseModel):
    TotalCost: float
    InternalCost: float
    ExternalCost: float
    Expenses: float


class BudgetInfo(BaseModel):
    BudgetDate_Use: datetime
    BudgetCost_Use: float



