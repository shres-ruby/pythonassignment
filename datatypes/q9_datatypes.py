# 9. Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 

word = list(input("Enter a string : "))
(word[0], word[-1]) = (word[-1], word[0])
result = ''.join(word)
print(result)