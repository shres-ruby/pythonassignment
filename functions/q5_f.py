# 5. Write a Python function to calculate the factorial of a number (a non-negative 
# integer). The function accepts the number as an argument. 

def fact(n):

    f = 1

    if n < 0:
        raise Exception("Negative integers are not accepted. Try again.")
    
    elif n == 0:
        print("The factorial is 1")
    
    else:
        for i in range (1,n+1):
            f *= i
    
    return f


result = fact(3)
print(f"The factorial is {result}")