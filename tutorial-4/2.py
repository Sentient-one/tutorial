class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == "__main__":
    rect1 = Rectangle(5, 3)
    print(f"Area of rectangle: {rect1.area()}")
    print(f"Perimeter of rectangle: {rect1.perimeter()}")