# 25. Write a Python program to check whether all dictionaries in a list are empty or not. 
# Sample list : [{},{},{}] 
# Return value : True 
# Sample list : [{1,2},{},{}] 
# Return value : False 

def emptycheck(l):
	for i in l:
		if len(i) == 0:
			return True
		else:
			return False

result = emptycheck([{1,2},{},{}])
print(result)