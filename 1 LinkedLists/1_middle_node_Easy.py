'''
You're given a Linked List with at least one node. 
Write a function that returns the middle node of the Linked List. 
If there are two middle nodes (i.e. an even length list), your function should return the second of it
'''


class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

'''
Approach:
	I'll be usiing fast-slow pointer approach.
'''
def middleNode(linkedList):
	fastPointer = slowPointer = linkedList
	
	while fastPointer and fastPointer.next:
		fastPointer = fastPointer.next.next
		slowPointer = slowPointer.next
	
	return slowPointer

'''
Time complexity: O(n)
Space Complexity: O(1)
'''
		
