# 2. Write a Python program to get a string made of the first 2 and the last 2 chars 
# from a given a string. If the string length is less than 2, return instead of the 
# empty string. 
# Sample String : 'Python' 
# Expected Result : 'Pyon' 
# Sample String : 'Py' 
# Expected Result : 'PyPy' 
# Sample String : ' w' 
# Expected Result : Empty String 

word = input("Enter a string : ")
if len(word) < 2:
	print ("Empty String")
else:
	print(word[:2] + word[-2:])