a=9

def something ():
    global a
    a=15
    print ("Inside" ,a)

something ()

print ("Outside" ,a)

#Appying global to a in function does not allow to chnage value to local a in function