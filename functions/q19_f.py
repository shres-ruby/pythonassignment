# 19. Write a Python program to create Fibonacci series upto n using Lambda.

n = int(input("Enter the number of terms : "))

f = [0,1]

list(map(lambda x: f.append(f[-1]+f[-2]), range(2,n)))

print(f)