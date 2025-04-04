class Arith:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    
    def read(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 == 0:
            return "Error: Division by zero"
        return self.num1 / self.num2


if __name__ == "__main__":
    a = Arith()
    a.read()
    print(f"Sum: {a.add()}")
    print(f"Difference: {a.subtract()}")
    print(f"Product: {a.multiply()}")
    print(f"Quotient: {a.divide()}")