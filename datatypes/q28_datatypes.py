# 28. Write a Python script to add a key to a dictionary. 
# Sample Dictionary : {0: 10, 1: 20} 
# Expected Result : {0: 10, 1: 20, 2: 30} 

dict = {0: 10, 1: 20}  

def addkey(k,v):
	dict.update({k : v})
	return dict

result = addkey(2,30)
print(result)