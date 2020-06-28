# 7. Write a Python function that takes a list of words and returns the length of the longest one.

def func(*args):
	for i in args:
		length = (len(i),)
	
	return max(length)

result = func('dog','puppy','watermelon')
print(result)