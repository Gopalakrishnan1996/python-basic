import sys

MAX_CHARS = 256

# Function to find smallest window containing
# all distinct characters
def findSubString(str):
    n = len(str)
    # Count all distinct characters.
    dist_count = 0
    hash_map = {}
    for i in range(n):
        if(str[i] in hash_map):

            hash_map[str[i]] = hash_map[str[i]] + 1
        else:
            hash_map[str[i]] = 1
    dist_count = len(hash_map)
    size = sys.maxsize
    res = 0
    # Now follow the algorithm discussed in below
    for i in range(n):
        count = 0
        visited = [0]*(MAX_CHARS)
        sub_str = ""
        for j in range(i, n):
            if (visited[ord(str[j])] == 0):
                count += 1
                visited[ord(str[j])] = 1

            sub_str += str[j]
            if (count == dist_count):
                break
        if (len(sub_str) < size and count == dist_count):
            res = sub_str
            size = len(res)
    return res
# Driver Code
# str = "aabcbcdbca"
str = input("Enter the input here: ")
print(
    f"Smallest window containing all distinct characters is: {findSubString(str)}")

