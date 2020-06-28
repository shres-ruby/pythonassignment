# 43. Write a Python program to remove an item from a tuple. 

t = (1,2,3,4,5)

r = list(t)
r.pop(1)
t = tuple(r)
print(t)