from numpy import *

# arr1= array([1,3,5,7,9])
#arr1=arr1+5
#print (arr1)

# arr1 = array ([2,6,8,3,7])
# arr1= sin (arr1)
# print (arr1)

# arr1= array ([1,4,7,2,4])
#  arr2= array ([2,6,3,4,5])

# arr3= arr1 + arr2
# print (arr3)


# Shallow copy of array 1


#arr1 = array ([2,6,9,4,7])
#arr2= arr1.view()

#arr1 [3]=16
#print(id(arr1))
# print(id(arr2))
#print (arr1)
#print (arr2)


#Deep copy
arr1 = array ([2,6,9,4,7])

arr2= arr1.copy() # any changes in arr1 does not affect arr2 even if we change values of arr1

arr1 [3]=16
print(id(arr1))
print(id(arr2))

print (arr1)
print (arr2)