class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print("Point destroyed")

p1 = Point(1,2)
print("Point is: %d, %d" % (p1.x,p1.y) )
del p1