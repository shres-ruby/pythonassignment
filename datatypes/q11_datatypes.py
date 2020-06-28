# 11. Write a Python program to count the occurrences of each word in a given sentence

sen = input("Please enter a sentence : ")

result = {}

for i in sen.split():
	count = sen.count(i)
	result.update({i: count})

print(result)