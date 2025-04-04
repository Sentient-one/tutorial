class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.cost = 0
    
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost
    
    def print_details(self):
        print("Book Details:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Cost: ${self.cost}")


book1 = Book()
book1.get_details("Python Programming", "John Smith", 45)
book1.print_details()

