from array import *

val=array ('i',[])

arr= int(input("Enter the size of an array"))


for i in range (arr):
    ele = int(input("Enter the next element"))
    val.append(ele)


print (val)

srch = int (input("Enter the element whose index you want to find "))
print(val.index(srch))