from Student import *

class SuperStudent(Student):
    def __init__(self):
        Student.__init__(self)
        self.value01 = 99
        self.value03 = 9999

    @staticmethod
    def mystaticmethod():
        print("SuperStudent.mystaticmethod")
