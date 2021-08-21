class Employee:
    def __init__(self,ID=None,salary=None,department=None):
        self.ID=ID
        self.salary=salary
        self.department=department
    def tax(self):
        return (self.salary*0.2)
    def salaryPerDay(self):
      return (self.salary/30)
steve=Employee(3789,2500,"HR")
print(steve.ID)
print(steve.salary)
print(steve.department)
print(steve.tax())
print(steve.salaryPerDay())
    
