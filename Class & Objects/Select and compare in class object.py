class Computer:
    def __init__(self):
        self.name="Varun"
        self.age=35

    def update(self):
        self.age=30
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False

c1=Computer()
c2=Computer()

if c1.compare(c2):
    print ("They are same")
else:
    print("They are not same")



c2.name="Rashi"

print(c1.age)
print(c2.age)