import csv

data = [
    ['Reg_no', 'Name', 'Sub_Mark1', 'Sub_Mark2', 'Sub_Mark3'],
    [10001, 'Jack', 76, 88, 76],
    [10002, 'John', 77, 84, 79],
    [10003, 'Alex', 74, 79, 81]
]

with open('student_marks.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data written to student_marks.csv")