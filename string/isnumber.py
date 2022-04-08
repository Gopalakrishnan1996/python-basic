def isNumber(s):
 
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
 
    return True
 
 
# Driver code
# Store the input in a str variable
# str = "6790"
str = input('enter a input here:')
# Function Call
if isNumber(str):
    print("Integer")
else:
    print("String")