# 10. Write a Python program to print the even numbers from a given list. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Expected Result : [2, 4, 6, 8] 

def iseven(list):
    
    result = []

    for i in list:
        if i % 2 == 0:
            result.append(i)
    
    return result

e = iseven([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(e)