class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
    
    def cost(self):
        print(f"The price of {self.model} ({self.year}) is ${self.price}")


car1 = Car("Toyota Camry", 2023, 25000)
car2 = Car("Honda Civic", 2024, 22000)

car1.cost()
car2.cost()