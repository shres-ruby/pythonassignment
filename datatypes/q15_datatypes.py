# 15. Write a Python function to insert a string in the middle of a string. 
# Sample function and result : 
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]] 
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}} 

def insert_string_middle(s,t):
	mid = int(len(s)/2)
	return s[:mid] + t + s[-mid:]

result = insert_string_middle('[[<<>>]]', 'Python')
print(result)