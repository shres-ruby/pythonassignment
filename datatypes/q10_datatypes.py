# 10. Write a Python program to remove the characters which have odd index values of a given string.

word = input("Enter a string : ")
lis = []

for i in range (len(word)):
	if (i%2) == 0:
		lis.append(word[i])
		result = ''.join(lis)
		
		
print(result)