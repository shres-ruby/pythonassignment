# 12. Write a Python program to create a function that takes one argument, and 
# that argument will be multiplied with an unknown given number. 

def func(n):

    def f():
        return n * 15

    return f

result = func(10)
print(result())