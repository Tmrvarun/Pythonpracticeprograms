from array import *

vals= array('i',[5,8,9,2,6])
newArr=array (vals.typecode,(a for a in vals))  # syntax for copying an array to a new array
newArr.reverse()
print (newArr)