# 4. Write a Python program to reverse a string. 
# Sample String : "1234abcd" 
# Expected Output : "dcba4321" 

def reverse(s):

    result = slice(-1,-len(s)-1,-1)
    return s[result]

result = reverse("1234abcd")
print(result)