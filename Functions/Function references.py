def val(x):
    print(id(x))
    x=8
    print ("New id of x: ",id(x))
    print ("x: ",x)

a=10
val (a)
print("a : ", a)
print(id(a))