def sum (a, *b):
    c=a
    for i in b:
        c=c+i
    print (c)

sum (5,4,17,37,8) #since b is tuple and a is integer so we can not add them straightaway, so we give *before b