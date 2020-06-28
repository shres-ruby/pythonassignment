# 8. Write a Python function that takes a list and returns a new list with unique 
# elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5] 
# Unique List : [1, 2, 3, 4, 5] 

def uniq(list):

    res = []

    for i in list:
        if i not in res:
	        res.append(i)

    return res

s = uniq([1,2,3,3,3,3,4,5])
print(s)