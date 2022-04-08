def removeSpaces(string):
    string = string.replace(' ','')
    return string
     
# Driver program
# string = "g  eeks  for ge  eeks  "
string = input("Enter the input here: ")
print(removeSpaces(string))