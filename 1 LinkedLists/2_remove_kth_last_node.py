'''
Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end of the list.
The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).
'''

class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

'''
I'll use two pointers to keep track of the positions.
Both will be initiated with head and a variable to keep track of nodes traversed.

I'll first iterate till the counter reaches k - (second pointer will be changed)
Now, in the other loop, first pointer will be iterated, untill second one reaches the end. 
In this way, we'll be to the n-kth position
'''
def removeKthNodeFromEnd(head, k):
	first = second = head
	counter = 1
	
	while counter <= k and second:
		counter += 1
		second = second.next
	# if we've reached the end, it means the length of the linkedlist is smaller, we'll just remove the first pointer
	if not second:
		head.value = head.next.value
		head.next = head.next.next
		return
	
	while second.next is not None:
		first = first.next
		second = second.next	
	
	first.next = first.next.next
		
	
