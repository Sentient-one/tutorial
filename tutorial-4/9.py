class RECTANGLE:
    def __init__(self, height, width, corner_x, corner_y):
        self.height = height
        self.width = width
        self.corner_x = corner_x  
        self.corner_y = corner_y  
    
    def center(self):
        center_x = self.corner_x + (self.width / 2)
        center_y = self.corner_y + (self.height / 2)
        return (center_x, center_y)
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


def create_rectangle(height, width, x, y):
    return RECTANGLE(height, width, x, y)


rect = create_rectangle(10, 5, 0, 0)


print(f"Rectangle center: {rect.center()}")
print(f"Rectangle area: {rect.area()}")
print(f"Rectangle perimeter: {rect.perimeter()}")