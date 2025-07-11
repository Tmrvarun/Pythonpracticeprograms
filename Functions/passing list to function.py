
def List (lst):
    even =0
    odd=0
    for i in lst:
        if (i%2==0):
            even+=1
        else:
            odd+=1
    return even,odd



lst= [1,3,4,6,8,9,12,35,67,80,3,3]
even,odd=List (lst)
print (even,odd)
