
def num():
    yield 10
    yield 23


values=num()
print(values.__next__())
print(values.__next__())
