from circle import circle
from rectangle import rectangle
from triangle import triangle

class main:
    def mainfun(self):
        print("This is main function")
        obj1 = circle()
        obj1.areac(10)
        obj1.peri(10)
        obj2 = rectangle()
        obj2.area(5,10)
        obj2.perimeter(5,10)
        obj3=triangle()
        obj3.areat(5,10)
        obj3.perimetert(5,10,5)


ob = main()
ob.mainfun()
