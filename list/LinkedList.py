class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function prints contents of linked list
	# starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next



# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
  n1 = int(input('Please enter 1st node:'))
  n2 = int(input('Please enter 2nt node:'))
  n3 = int(input('Please enter 3rd node:'))
  llist = LinkedList()
  llist.head = Node(n1)
  second = Node(n2)
  third = Node(n3)
  llist.head.next = second; # Link first node with second
  second.next = third; # Link second node with the third node
  llist.printList()
