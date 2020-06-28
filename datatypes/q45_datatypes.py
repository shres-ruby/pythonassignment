# 45. Write a Python program to find the index of an item of a tuple. 

def tup(tuple, x):

    return tuple.index(x)

t = ('p','y','t','h','o','n')

result = tup(t,'h')
print(f"The index of is {result}")