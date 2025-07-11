class Car:
    wheels=4 #Class variable
    def __init__(self):
        self.name="AUDI" #instance variable
        self.mil= 15

c1=Car()
c2=Car()

print(c1.name,c1.mil,c1.wheels)
print(c2.name,c2.mil,c1.wheels)