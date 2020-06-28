# 3. Write a Python program to get a string from a given string where all 
# occurrences of its first char have been changed to '$', except the first char itself. 
# Sample String : 'restart' 
# Expected Result : 'resta$t' 

word = input("Please enter a string : ")

first = word[0]

for i in word[1:]:
	if i == first:
		result = word[1:].replace(i,"$")
		print(first+result)
		break

else:
	print(word)