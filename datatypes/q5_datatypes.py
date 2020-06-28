# 5. Write a Python program to add 'ing' at the end of a given string (length should 
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the 
# string length of the given string is less than 3, leave it unchanged. 
# Sample String : 'abc' 
# Expected Result : 'abcing' 
# Sample String : 'string' 
# Expected Result : 'stringly' 

word = input("Please enter a string : ")

if len(word) >= 3:
	if word[-3:] == "ing":
		print(word+"ly")
	
	else:
		print(word+"ing")

else:
	print (word)