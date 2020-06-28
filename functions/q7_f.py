# 7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
# Sample String : 'The quick Brow Fox' 
# Expected Output : 
# No. of Upper case characters : 3 
# No. of Lower case Characters : 12 

def func(s):
    upper = 0
    lower = 0

    for i in s:
        if i.isupper() == True:
            upper += 1

        elif i.islower() == True:
            lower += 1
    
    return upper, lower
    # print(f"No. of Upper case characters : {upper}\nNo. of Lower case characters : {lower}")

upper,lower = func('The quick Brow Fox')
print(f"No. of Upper case characters : {upper}")
print(f"No. of Lower case characters : {lower}")