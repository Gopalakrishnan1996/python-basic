MAX_CHAR = 26

# Returns characters that needs
# to be added to make str
def missingChars(Str):
	
	# A boolean array to store characters
	# present in string.
	present = [False for i in range(MAX_CHAR)]

	# Traverse string and mark characters
	# present in string.
	for i in range(len(Str)):
		if (Str[i] >= 'a' and Str[i] <= 'z'):
			present[ord(Str[i]) - ord('a')] = True
		elif (Str[i] >= 'A' and Str[i] <= 'Z'):
			present[ord(Str[i]) - ord('A')] = True

	# Store missing characters in alphabetic
	# order.
	res = ""

	for i in range(MAX_CHAR):
		if (present[i] == False):
			res += chr(i + ord('a'))
			
	return res

# Driver code
Str = input('enter a input here:')
# Str = "The quick brown fox jumps over the dog"

print(missingChars(Str))


