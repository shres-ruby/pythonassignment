# 13. Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
 
t = input("Please enter a few words : ").split(",")
result = list(dict.fromkeys(sorted(t)))
print(result)