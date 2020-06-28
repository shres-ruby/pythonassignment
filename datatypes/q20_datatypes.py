# 20. Write a Python program to count the number of strings where the string length is 2 or more and the first and 
# last character are  same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221'] 
# Expected Result : 2 

inp = input("Enter some strings separated by comma : ").split(",")
count = 0
for i in inp:
	j = i.lstrip()
	if j[0] == j[-1]:
		count += 1

print(count)