class Student:
    school = "IIT Delhi"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def calc(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is static method")


s1 = Student(56, 78, 87)
s2 = Student(71, 79, 88)
print(s2.calc())
print(s1.calc())
print(Student.getSchool())
Student.info()
