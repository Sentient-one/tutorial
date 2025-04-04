class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    
    def dataprint(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")


student1 = Student("John Smith", "A123")
student2 = Student("Emma Johnson", "B456")

print("First student details:")
student1.dataprint()
print("\nSecond student details:")
student2.dataprint()