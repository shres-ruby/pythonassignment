# 16. Write a Python program to square and cube every number in a given list of
# integers using Lambda.

l = [2,3,4,5,6]

sq = list(map(lambda x: x**2, l))
cb = list(map(lambda x: x**3, l))

print(f"The square of every number in the list : {sq}")
print(f"The cube of every number in the list : {cb}")