class A:
    def feature1 (self):
        print ("Feature 1 is ready ")

    def feature2 (self):
        print ("Feature 2 is ready")

class B:
    def feature3 (self):
        print ("Feature 3 is ready")
    def feature4 (self):
        print ("Feature 4 is ready")

class C (A,B):
    def feature5 (self):
        print("Feature 5 is ready")
    def feature6 (self):
        print ("Feature 6 is ready")

a1=A()
a1.feature1()
a1.feature2()

b1=B() #class B inherits all features of class A and is called hierarchial/single level inheritance
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature3()

c1=C()  #Class C inherits A &B but b does not inherits any class so it is called multiple inheritance
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()