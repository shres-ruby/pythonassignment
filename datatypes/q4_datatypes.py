# 4. Write a Python program to get a single string from two given strings, separated 
# by a space and swap the first two characters of each string. 
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz' 

word1 = input("Enter the first string : ")
word2 = input ("Enter the second string : ")

first = word1.replace(word1[:2], word2[:2])
second = word2.replace(word2[:2], word1[:2])

print (first + ' ' + second)