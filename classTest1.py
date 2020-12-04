class Employee:
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount+=1


    def dispCount(self):
        print("No od employess: %d "% Employee.empCount)

    def dispEmployee(self):
        print("Employee Name: %s ,Salary: %d " % (self.name,self.salary))

emp1 = Employee("Jack", 50000)
emp1.dispEmployee()
#emp1.dispCount()

emp2 = Employee("Zara",60000)
emp2.dispEmployee()
emp2.dispCount()

#hasattr(emp1,'salary')
print("Age exist: " + str(hasattr(emp1,'age')))
print("Salary exist: "+ str(hasattr(emp1,'salary')))
setattr(emp1,'age',25)
print("Age is:%d " % emp1.age)
#print("Age is:%d " % emp2.age)
print("Slary is: "+ str(getattr(emp2,'salary')))

delattr(emp1,'age')
print("Age exist: " + str(hasattr(emp1,'age')))

print("Employee doc: ",Employee.__doc__)
print("Employee.__name__: ",Employee.__name__)
print("Employee.__module__: ",Employee.__module__)
print("Employee.__bases__",Employee.__bases__)
print("Employee.__dict__",Employee.__dict__)

