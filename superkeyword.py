class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        print("These are the properties of parent class rectangle")
class square(rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)

    def area(self):
        return self.length*self.width

class cube(rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = 3
        self.heigth=height
    def volume(self):
         return self.length*self.width*self.height

square = square(3,3)
cube = cube(3 ,3, 3)

print(square.area())
print(cube.volume())