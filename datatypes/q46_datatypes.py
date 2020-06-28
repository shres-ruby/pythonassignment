# 46. Write a Python program to find the length of a tuple 

def tup(*args):
    
    return len(args)

result = tup(1,2,3,4,5)
print(result)