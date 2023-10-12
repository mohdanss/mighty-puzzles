'''Statement:
You are given a head node of the singly linkedlist, nodes are sorted, with respect to it's values.
You need to write a function, that takes in that head node, and removes the duplicates from that list.

Example:
input: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> 5
output: 1 -> 2 -> 3 -> 4 -> 5

Note: solution should be in-place, the result should also be in sorted form.
Each LinkedList Node has a value and a pointer to the next node (which can be None/null too)
'''

class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

'''
Approach:
Overall: I'll iterate over the list, starting from head abvoiusly.
While I don't reach the end of the list, I'll keep checking:
	If the current node's value is same as it's next one:
		If it is, remove the duplicate, but pointing current.next to current.next.next node
	and point the node to next; of current
In the end, I'll return the same head I've got as argument.

Step 0 - Edge cases:
	To prevent the code from crashing, I'll need to take into account of handling nodes which are null/None.

Step 1 - Initialize two variables that'll point to the current node and the previous node.
	currentNode = linkedlist
	
Step 2 - Iterate over the list:
	while currentNode.next is not None:
		if currentNode.value == currentNode.next.value:
			currentNode.next = currentNode.next.next
		else:
			currentNode = currentNode.next
return linkedlist
'''
def removeDuplicatesFromLinkedList(linkedlist):
	if linkedlist is None:
		return linkedlist
	
	currentNode = linkedlist

	while currentNode.next is not None:
		if currentNode.value == currentNode.next.value:
			currentNode.next = currentNode.next.next
		else:
			currentNode = currentNode.next
	return linkedlist

'''
	Time Complexity: O(n)
	Space Complexity: O(1)
'''
