# 8. Write a Python program to remove the nth index character from a nonempty string. 

s = input("Enter a string : ")

if len(s) > 0:
	i = int(input("Enter the number of the index character to be removed : "))
	rem = s[i]
	result = s.replace(rem, '')
	print(result)

else:
	print("This field cannot be empty. Please try again.")