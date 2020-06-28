# 30. Write a Python script to check whether a given key already exists in a dictionary. 

dict = {"name": "ram" , "gender": "m", "age": 21, "address": "ktm"}

key = input("Enter a key to check : ")

if key in dict.keys():
	print("That key already exists")
else:
	print("Key not found in dictionary")