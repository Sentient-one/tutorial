def find_quadrant(x, y):
    """Find the quadrant of point (x, y)"""
    if x > 0 and y > 0:
        return "First Quadrant (I)"
    elif x < 0 and y > 0:
        return "Second Quadrant (II)"
    elif x < 0 and y < 0:
        return "Third Quadrant (III)"
    elif x > 0 and y < 0:
        return "Fourth Quadrant (IV)"
    elif x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "Y-axis"
    else:  
        return "X-axis"


x = float(input("Enter x: "))
y = float(input("Enter y: "))

print(f"The point ({x}, {y}) is in the {find_quadrant(x, y)}.")