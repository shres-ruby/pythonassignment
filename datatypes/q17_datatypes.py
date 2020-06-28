# 17. Write a Python program to multiplies all the items in a list. 

num = input("Enter some numbers separated by comma : ").split(",")
p = 1
for i in num:
	p *= int(i)
print(p)