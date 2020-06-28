# 14. Write a Python program to sort a list of dictionaries using Lambda.

d = [{"name" : "sita", "gender" : "female", "address" : "kathmandu"}, 
    {"name" : "ram", "gender" : "male", "address" : "kathmandu"},
    {"name" : "hari", "gender" : "male", "address" : "kathmandu"}]


res = sorted(d, key= lambda x: x['name'])
print(res)