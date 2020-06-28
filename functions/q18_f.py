# 18. Write a Python program to check whether a given string is number or not using Lambda.

num = "423423453"

result = lambda x: x.isdigit()

print(result(num))