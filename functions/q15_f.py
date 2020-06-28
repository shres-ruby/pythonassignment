# 15. Write a Python program to filter a list of integers using Lambda.

li = [1,2,3,4,5,6,7,8,9,10]

# filtering out even numbers from the list
result = list(filter(lambda x: x % 2 == 0, li))
print(result)