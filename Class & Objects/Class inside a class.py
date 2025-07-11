class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop() #we are accessing the laptop objects here

    def show(self):
        print(self.name,self.rollno)
        self.lap.show() #since laptop is within student class

    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.storage=256
            self.ram=16

        def show(self):
            print(self.brand,self.storage,self.ram)

s1=Student('Varun Tomar',7932)
s2=Student('Rajesh', 256)


s1.show()
s2.show()