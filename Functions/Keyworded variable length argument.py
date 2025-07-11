
def person (name , **data):
    print (name)
    #print (data)

    for i,j in data.items(): # to print keywords we used this loop
        print (i,j)


person ('Varun' , age=28 , city ='Noida' , mob = 9807123)