from numpy import *

arr1=array ([
        [1,2,3,5,7,5],
        [2,4,6,9,5,1]
        ])
print (arr1.ndim)
arr2 = arr1.flatten()
# arr3= arr2.reshape(3,4) (Resize array 2 into 3 row and 4 column)

arr3 = arr1.reshape(2,2,3) #Will create 2 matrix of 2 row and 3 column each
print (arr3)
