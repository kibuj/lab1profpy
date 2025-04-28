class Student:
    def __init__(self, name, e1, e2, e3):
        self.name = name
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def get_average_mark(self):

        print(self.name, ' - ', ((self.e1 + self.e2 + self.e3) / 3))

students = []
n = int(input("Яка кількість студентів?\n"))

for i in range(n):
    name = input(f"Ім'я студента - №{i + 1}:\n")
    e1 = int(input(f'1-ий бал\n'))
    e2 = int(input(f'2-ий бал\n'))
    e3 = int(input(f'3-ий бал\n'))

    student = Student(name, e1, e2, e3)
    students.append(student)

for j in students:
    j.get_average_mark()
