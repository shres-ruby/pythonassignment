# 3. Write a Python function to multiply all the numbers in a list. 
# Sample List : (8, 2, 3, -1, 7) 
# Expected Output : -336 

def product(list):
    
    result = 1
    for item in list:
        result *= item
    
    return result

result = product([8,2,3,-1,7])
print(f"The product of the numbers is : {result}")