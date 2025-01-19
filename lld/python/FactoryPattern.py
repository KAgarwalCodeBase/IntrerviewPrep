from abc import ABC, abstractmethod 
import math 

# Abstract Shape Class
class Shape(ABC):
    @abstractmethod 
    def getPerimeter(self):
        pass
    @abstractmethod
    def getArea(self):
        pass

# Concrete Classes
class Circle(Shape):
    def __init__(self, radius=3):
        self.radius = radius
    def getArea(self):
        return round(math.pi*self.radius*self.radius,2)
    def getPerimeter(self):
        return round(2*math.pi*self.radius, 2)
            

class Square(Shape):
    def __init__(self, side=3):
        self.side = side
    
    def getArea(self):
        return self.side * self.side 

    def getPerimeter(self):
        return 4*self.side
    
# Factory Class
class ShapeFactory:
    @staticmethod
    def getShape(shape):
        if not isinstance(shape, str):
            return 'Not Valid Input'
        if shape=='circle':
            return Circle()
        elif shape=='square':
            return Square()
        
# Client Code
if __name__=='__main__':
    # create circle
    circle = ShapeFactory.getShape('circle')
    print('Perimeter of Circle: ',circle.getPerimeter())
    print('Area of Circle: ',circle.getArea())
    
    # create square
    square = ShapeFactory.getShape('square')
    print('Perimeter of Circle: ',square.getPerimeter())
    print('Area of Square: ', square.getArea())