
def countNonEmptySubstr(str):
	n = len(str)
	return int(n * (n + 1) / 2)

# driver code
# s = "abcde"
str = input("Enter the input here:")
print (countNonEmptySubstr(str))

