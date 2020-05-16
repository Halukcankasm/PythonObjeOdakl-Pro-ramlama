"""
OOP:OBject Oriented Programing
    - class/onject
    -attribute/methods
    -encapsulation/abstraction
    -inheritance
    -overriding/polymorphism
    
"""
from abc import ABC , abstractmethod

class Shape(ABC):
    """
    Shape = super class / abstract class
    """
    
    
    @abstractmethod
    def area(self):pass
    
    @abstractmethod
    def perimeter(self):pass

    def toString():pass


class Square(Shape):
    
    def __init__(self,side):
        self.__side=side
    
    def area(self):
        Area=self.__side*self.__side
        print("Square area:",Area)

    def perimeter(self):
        Perimeter=4*self.__side
        print("Square perimeter",Perimeter)
    
    
class Circle(Shape):
    
    def __init__(self,radius):
        self.__radius=radius
    
    def area(self):
        Area=self.__radius**2*3.14
        print("Circle area:",Area)

    def perimeter(self):
        Perimeter=2*3.14*self.__radius
        print("Circle perimeter:",Perimeter)
    
c1=Circle(5)

s1=Square(5)


shapeList=[c1,s1]
for shape in shapeList:
    shape.area()
    shape.perimeter()
    
    

    