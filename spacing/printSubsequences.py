from math import pow

def printSubsequences(str):
	n = len(str)
	opsize = int(pow(2, n - 1))

	for counter in range(opsize):
		for j in range(n):
			print(str[j], end = "")
			if (counter & (1 << j)):
				print(" ", end = "")

		print("\n", end = "")

# Driver code
if __name__ == '__main__':
	# str = "ABC"
  str = input("Enter the input here: ")
  printSubsequences(str)
