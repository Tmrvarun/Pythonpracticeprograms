class A:
    def __init__(self):
        print ("Constructor of A")

    def feature1(self):
        print ("This is feature 1 of class A")

class B:
    def __init__(self):
        super().__init__()
        print("Constructor of B")


    def feature1(self):
        print("This is feature 1 of class B")

class C(A,B):
    def __init__(self):

        super().__init__()
        print("Constuctor of C")


a1=C()

