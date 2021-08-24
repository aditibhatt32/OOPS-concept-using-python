class Employee:
    
         
    def demo(self,a,b,c,d=5,e=None):
     print("a=",a)
     print("b=",b)
     print("c=",c)
     print("d=",d)
     print("e=",e)

    def tax(self,title=None):
     return self.salary*0.2

    def salaryPerDay(self):
     return (self.salary/30)

Steve=Employee()
print("Demo1")
print(Steve.demo(1,2,3))
print("\n")
print("Demo2")
print(Steve.demo(1,2,3,4))
print("\n")

print("Demo3")
print(Steve.demo(1,2,3,4,5))
 
