'''
    Write a function that takes in a non-empty array of integers that are sorted in ascending order (1,2,3) and returns a new array of the same length with the squares of the original integers also sorted in ascending order.

    Sample:
        input: [1,2,3,5,6,8,9]
        output: [1,4,9,25,36,64,81]

        input: [-2, -1]
        output: [1,4]

    Note: input array shouldn't be modified

    -> Make sure to make it as optimized as possible, both time and space complexity wise.
    -> Take a deep breath, put aside your 'imposter-self', and give it a go ;)
'''


def sortedSquaredArray(array):
    squaredArray = [0] * len(array)
    leftPtr = 0
    rightPtr = len(array) - 1
    maxElementPosition = rightPtr

    while leftPtr <= rightPtr:
        leftAbsValue = abs(array[leftPtr])
        rightAbsValue = abs(array[rightPtr])

        if leftAbsValue > rightAbsValue:
            squaredArray[maxElementPosition] = leftAbsValue**2
            leftPtr += 1
        else:
            squaredArray[maxElementPosition] = rightAbsValue**2
            rightPtr -= 1
        maxElementPosition -= 1

    return squaredArray


print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9])
      == [1, 4, 9, 25, 36, 64, 81])
print(sortedSquaredArray([-2, -1]) == [1, 4])
print(sortedSquaredArray([-10, -5, 0, 5, 10]) == [0, 25, 25, 100, 100])


'''
Appraoch:
    As we are not allowed to change input array. 
    Create a new array of size n, initialized with 0,

    Now, use two pointer appraoch (as input array is sorted), pointing to left and right side of the array. 
    Take the maximum absolute value and place the squared value in the output array.

    keep doing untill left and right pointers don't meet.

Algorithm:
    outputArr = [0] * size of array
    leftPtr = 0
    rightPtr = size of array - 1

    maxElementPosition = n - 1 #start filling from the right

    while leftPtr <= rightPtr:
        leftAbsValue = abs(array[leftPtr])
        rightAbsValue = abs(array[rightPtr])

        if rightAbsValue < leftAbsValue:
            array[maxElementPosition] = square(leftAbsValue)
            leftPtr += 1
        elif rightAbsValue >= leftAbsValue:
            array[maxElementPosition] = square(rightAbsValue)
            rightPtr -= 1
        maxElementPosition -= 1

Time: O(n) - as a single traversal took place.
Space: O(n) - for storing the output array.
'''
