# 13. Write a Python program to sort a list of tuples using Lambda.

l = ([(45,78),(34,4),(2,67)])
result = sorted(l, key = lambda x: x[0])
print(result)