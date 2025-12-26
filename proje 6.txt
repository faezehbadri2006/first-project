from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def init(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def init(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14159 * (self.radius ** 2)
    
    def calculate_perimeter(self):
        return 2 * 3.14159 * self.radius

shapes = [
    Rectangle(5, 3),
    Circle(4)
]

for shape in shapes:
    print(f"masahat: {shape.calculate_area()}")
    print(f"mohit: {shape.calculate_perimeter()}")
    print("---")