num=[1,2,3,4,6]

itr=iter(num)


for i in num:
    print(itr.__next__())