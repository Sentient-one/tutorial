class Mobile:
    def __init__(self):
        self.company = ""
        self.model = ""
        self.price = 0
    
    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price
    
    def display_details(self):
        print("Mobile Details:")
        print(f"Company: {self.company}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")


mobile1 = Mobile()
mobile1.set_details("Samsung", "Galaxy S23", 999)
mobile1.display_details()