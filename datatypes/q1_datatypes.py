# 1) Write a Python program to count the number of characters (character 
# frequency) in a string. Sample String : google.com' 
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 

g = "google.com"
result = {}

for i in g:
	count = g.count(i)
	result.update({i: count})

print (result)