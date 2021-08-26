class Employee:
    def __init__(self,ID,salary):
        self.ID=ID
        self.__salary=salary
steve=Employee(3789,2500)
print("ID:",steve.ID)
print("salary:",steve.__salary)
