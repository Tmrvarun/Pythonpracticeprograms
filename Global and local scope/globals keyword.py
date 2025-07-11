a=9
print (id(a))
def something ():
    a=12
    x=globals()['a']
    print (id(x))
    print (a)


something()

print ("Outside ", a)