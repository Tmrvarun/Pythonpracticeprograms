class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1=Student(34,55)
print(s1.sum(3,7,9))

#Method overloading is not supported in python, so we use None in the method sum to match the parameter passed in object sum

#Method overriding is achived by inheritance in python , in other languages like java we achieve this stste when we use same method name and same parameter