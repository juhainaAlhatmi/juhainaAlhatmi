from employee_models import Money
from money import Money

class Money:

  def __init__(self,InternalCost,externalCost):
    self.EnternalCost= InternalCost
    self.externalCost = externalCost


c1=input(float("Enter Internal Cost : ",InternalCost))
c2=input(float("Enter Internal Cost : ",externalCost))

TotalCost = c1 + c2

print(c1.InternalCost)

print(c2.externalCost)

print(TotalCost)
