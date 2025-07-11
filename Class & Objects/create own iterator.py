class  iterator:
    def __init__(self):
        self.num=1
    def __iter__(self): #This function/method is used to return value of iteratiom
        return self
    def __next__(self): #This method/function is used to get the next value of iterator
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration

value=iterator()
for i in value:
    print(i)