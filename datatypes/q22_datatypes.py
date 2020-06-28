# 22. Write a Python program to remove duplicates from a list. 

lis = input("Enter some values separated by comma : ").split(",")

res = []

for i in lis:
    if i not in res:
	    res.append(i)

print(res)