# 20. Write a Python program to find intersection of two given arrays using Lambda.

l1 = [43, 9, 0, 17, 11, 26, 28, 54, 88]
l2 = [77, 9, 9, 74, 21, 45, 11, 63, 28, 26]

r = list(filter(lambda x: x in set(l1), set(l2)))

print(r)