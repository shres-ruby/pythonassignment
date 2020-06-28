# 6. Write a Python function to check whether a number is in a given range. 

def range_check(n):

    if n in x:
        return "The number is in range"
    
    elif n not in x:
        return "The number is out of range"


x = (1,2,3,4,5,6,7,8,9,10)

result = range_check(7)
print(result)