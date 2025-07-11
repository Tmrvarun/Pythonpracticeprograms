from numpy import *

m1= matrix ('1 2 3 ; 4 5 7 ; 3 8 3 ')
m2= matrix ('1 2 5 ; 4 6 9 ; 3 8 5')
m3= m1 *m2
print (m1.diagonal()) #gives diagonal element of matrix

print (m1.max())
print (m1.min())

print (m3)