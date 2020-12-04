class Parent:
    var = 100
    def __init__(self):
        print("Calling parent constructor")

    def display(self):
        print("Calling parent method")

    def __setattr__(self, attr):
        Parent.var = attr
    def __getattr__(self):
        print("Value is: ",Parent.var)

class Child(Parent):
    def __init__(self):
        print("Caling child constructor")

    def disp(self):
        print("Calling child method")

c = Child()
c.disp()
c.display()



