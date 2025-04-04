class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: ${self.salary}")


person1 = Person("Alice Brown", 28, 55000)
person2 = Person("Bob Wilson", 35, 68000)

print("First person details:")
person1.display()
print("\nSecond person details:")
person2.display()