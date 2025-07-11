from functools import reduce

lst=[2,5,7,9,3,5,8,6,4,10]
even= list(filter (lambda n:n%2==0,lst))
print (even)

double= list(map(lambda n:n*2,even))
print (double)

sum= reduce(lambda a,b: a+b, double)
print (sum)