a=10 #global value


def something():
    a=15 #local value
    print ("Function value", a)

something()

print ("Outside value",a)

#When we run this code local variable execute first rather than global