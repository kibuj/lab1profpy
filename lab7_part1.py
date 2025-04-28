class Student:

    def set_marks(self, e1, e2, e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3


    def set_name(self, name):
        self.name = name


    def get_average_mark(self):

        print(self.name, ' - ', ((self.e1 + self.e2 + self.e3) / 3))

s1 = Student()
s2 = Student()

s1.set_name('Dmytro')
s1.set_marks(5, 4, 5)
s1.get_average_mark()

s2.set_name('Mykola')
s2.set_marks(4, 4, 4)
s2.get_average_mark()