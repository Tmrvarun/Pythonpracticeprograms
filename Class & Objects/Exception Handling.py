a=5
b=2

try:
    k = int(input("Enter value"))
    print(k)
    print(a/b)
    print("Resource open")


except ValueError as e:
    print ("Enter a number not character",e)
except Exception as e:
    print("The number can not be divide by 0" , e)
except ZeroDivisionError as e:
    print("Change number from 0 to some other", e)

finally:
        print("Resource Closed")

