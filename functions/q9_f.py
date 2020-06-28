# 9. Write a Python function that takes a number as a parameter and check the number is prime or not. 
# Note : A prime number (or a prime) is a natural number greater than 1 and that 
# has no positive divisors other than 1 and itself. 

def isprime(n):

    if n < 2:
        raise Exception("Please enter a number greater than 1")
    
    elif n >= 2:
        for i in range(2,n):
            if n % i == 0:
                return("Not prime")
                break

        else:
            return("Prime")
    

print(isprime(2))