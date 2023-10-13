'''
You're given two Linked Lists of potentially unequal length. 
Each Linked List represents a non-negative integer, 
where each node in the Linked List is a digit of that integer, 
and the first node in each Linked List always represents the least significant digit of the integer. 

Write a function that returns the head of a new Linked List that represents the sum of the integers represented by the two input Linked Lists.

Example:

input:
ll1 = 2 -> 4 -> 7 -> 1
ll2 = 9 -> 4 -> 5

result = 1 -> 9 -> 2 -> 2
'''

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
	newListHead = currNode = LinkedList(0)
	carry = 0
	ptrLLOne = linkedListOne
	ptrLLTwo = linkedListTwo

	while ptrLLOne or ptrLLTwo:
		newValue = carry
		
		if ptrLLOne:
			newValue += ptrLLOne.value
		if ptrLLTwo:
			newValue += ptrLLTwo.value
		
		carry = newValue // 10 if newValue > 9 else 0
		newValue = newValue % 10

		ptrLLOne = ptrLLOne.next if ptrLLOne else None
		ptrLLTwo = ptrLLTwo.next if ptrLLTwo else None
		
		currNode.next = LinkedList(newValue)
		currNode = currNode.next
		
	if carry > 0:
		currNode.next = LinkedList(carry)
	
	return newListHead.next

'''
Time Complexity: O(max(m,n))
Space Complexity: O(max(m,n))
'''
