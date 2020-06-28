# 34. Write a Python script to merge two Python dictionaries. 

def dic(**data):
    
    d = {}

    for k,v in data.items():
        d.update({k : v})
    return d

dict1 = dic(name ="ram", address = "ktm", age = 20)
dict2 = dic(a="apple" , b="ball", c="cat")
dict1.update(dict2)
print(dict1)