# 16. Write a Python program to sum all the items in a list. 

num = input("Enter some numbers separated by comma : ").split(",")
sum = 0
for i in num:
	sum += int(i)
print(sum)