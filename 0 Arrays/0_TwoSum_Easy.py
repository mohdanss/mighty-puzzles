'''
    Write a function that takes in a non-empty array of unique numbers, and an integer representing target sum. If any two numbers in the array sum up to that target number, return those numbers.

    For example:
    array = [1,2,3,4,5]
    targetSum = 3

    returned value should be a list containing both numbers, in the case above:
    return value = [1,2]

    make sure to make it as optimized as possible, both time and space complexity wise.
    Take a deep breath, put aside your 'imposter-self', and give it a go ;)
'''

def twoNumberSum(array, targetSum):
    exploredSet = set()
    for number in array:
        potentialMatch = targetSum - number

        if potentialMatch in exploredSet:
            return [potentialMatch, number]
        exploredSet.add(number)
    return []

'''
Time and space complexity analysis:
Our code iterate n times, and each time it checks for the number which can potentialy be a match for the pair, it is checking that from the set, and time for retreival something in the set is O(1).
Time Complexity: O(n)

It is maintaining an explore set, so it is taking up the space of n elements. 
Space Complexity: O(n)
'''