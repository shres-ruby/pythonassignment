# 2. Write a Python function to sum all the numbers in a list. 
# Sample List : (8, 2, 3, 0,7) 
# Expected Output : 20 

def listsum(list):
    
    return sum(list)

result = listsum([8,2,3,0,7])
print(f"The sum of the numbers in the list is : {result}")