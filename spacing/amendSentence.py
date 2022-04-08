def amendSentence(string):
	string = list(string)

	# Traverse the string
	for i in range(len(string)):

		# Convert to lowercase if its
		# an uppercase character
		if string[i] >= 'A' and string[i] <= 'Z':
			string[i] = chr(ord(string[i]) + 32)

			# Print space before it
			# if its an uppercase character
			if i != 0:
				print(" ", end = "")

			# Print the character
			print(string[i], end = "")

		# if lowercase character
		# then just print
		else:
			print(string[i], end = "")

# Driver Code
if __name__ == "__main__":
  # string = "BruceWayneIsBatman"
  string = input("Enter the input here: ")
  amendSentence(string)

