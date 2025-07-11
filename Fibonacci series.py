


def fib (x):
    a=0
    b=1

    if (x==0):
        print (a)
    else:
        print(a)
        print(b)
        for i in range(2,x):
            c=a+b
            a=b
            b=c
            if (c>100):
                break
            else:
                print(c)



x=int(input("Enter the number of values you want to see in the series"))
fib (x)