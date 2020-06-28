# 18. Write a Python program to get the largest number from a list. 

lt = []

num = int(input("How many numbers do you want to enter? "))

for i in range (1,num+1):
	inp = int(input("Enter a number : "))
	lt.append(inp)

lt.sort()
print(f"The largest number is : {lt[-1]}")