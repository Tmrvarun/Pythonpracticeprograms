lst=[12,3,56,89,2,5]

print (max(lst))
print(min(lst))
lst.insert(2,35)
lst.append(85)
lst.remove(89)
print (lst)

tupl=(1,2,5,71,54,65)
print(tupl)
print(tupl[1]==3)
print(tupl[3])
tupl

dic={1:'Varun',2:'Tarun'}
print(dic[1])
print(dic.get(1,'Not Found')) #If no value is found then this output is printed

key =['Varun','Rahul','Tarun']
value=['Java','Python','C#']
data=dict(zip(key,value))

print(data['Rahul'])
data['Monika']='AI'
print(data)
print(data['Monika'])

