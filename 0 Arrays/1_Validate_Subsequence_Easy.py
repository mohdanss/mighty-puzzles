'''
    Given two non empty array of integers, find out using a function whether the 2nd array is subsequennce of other or not.
    
    A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array. 
    
    For example,
    array =  [1, 2, 3, 4]
    sequence = [1, 3, 4] 
    
    Here, array2 forms a subsequence of the array2.
    and so do the numbers [2, 4]. 
    Note that a single number in an array and the array itself are both valid subsequences of the array.

    make sure to make it as optimized as possible, both time and space complexity wise.
    Take a deep breath, put aside your 'imposter-self', and give it a go ;)
'''

def isValidSubsequence(array, sequence):
    ptrArray = ptrSequence = 0

    while ptrArray < len(array) and ptrSequence < len(sequence):
        if array[ptrArray] == sequence[ptrSequence]:
            ptrSequence += 1
        ptrArray += 1 

    return ptrSequence == len(sequence)

print(isValidSubsequence([1,2,3,4],[1,3,4]) == True)
print(isValidSubsequence([1,2,3,4],[2,4]) == True)
print(isValidSubsequence([5,1,22,25,6,-1,8,10],[1,6,-1,10]) == True)
print(isValidSubsequence([5,1,22,25,6,-1,8,10],[1,6,-1,25]) == False)


'''
Q: can I do this in single traverse?
A: yes

Approach:
I'll take two pointers, 1 for array, other for sequence.

ptrArray = ptrSequence = 0

LOOP untill - ptrArray < len(array) || ptrSequence < len(sequence):
    if array[ptrArray] is equal to sequence[ptrSequence]:
        increment both pointers
    else:
        increment array pointer
    
    return true if ptrSequence is equal to len(sequence) else false

A single traversal was done, so the time complexity is O(n) - n is length of array
No extra space used, space complexity is O(1)
'''