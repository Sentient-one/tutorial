class Student:
    def __init__(self):
        self.rollno = 0
        self.mark1 = 0
        self.mark2 = 0
        self.total = 0
    
    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2
    
    def computeTotal(self):
        self.total = self.mark1 + self.mark2
        return self.total
    
    def printDetails(self):
        print("Student Details:")
        print(f"Roll No: {self.rollno}")
        print(f"Mark 1: {self.mark1}")
        print(f"Mark 2: {self.mark2}")
        print(f"Total Marks: {self.total}")


student1 = Student()
student1.readData(101, 85, 92)
student1.computeTotal()
student1.printDetails()