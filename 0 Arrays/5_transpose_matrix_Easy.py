'''
Description: You're given a 2D array of integers, a matrix, write a function that returns the transpose of that matrix


Sample I/O:
matrix = [1]
transpose_matrix = [1]

matrix = [1, 2]
transpose_matrix = [
    [1],
    [2]
]

matrix = [
    [1],
    [2],
    [3]
]

transpose_matrix = [
    [1,2,3]
]

-> Make sure to make it as optimized as possible, both time and space complexity wise.
-> Take a deep breath, put aside your 'imposter-self', and give it a go ;)
'''

# code
def transposeMatrix(matrix):
    transpose_matrix = []

    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transpose_matrix.append(newRow)

    return transpose_matrix


print(transposeMatrix([[1]]) == [[1]])
print(transposeMatrix([[1,2]]) == [[1],[2]])
print(transposeMatrix([[1],[2],[3]]) == [[1, 2, 3]])
'''
Analysis: For solving, just visualize a mathematical matrix,
You need to convert 
ROW into COLUMNS or
COLUMNS into ROW

In this code, we are initializing the empty array, that'll hold the transpose,
So here we'll be using O(COL * ROWS) space!

Then we'll iterate each for:
EACH COLUMN WITHIN ROW - 

We need to visualize in mind:
- We need to create a matrix that has same number of rows as columns -

This code iterates through each column of the input matrix, collects the elements from each column into a new row, and assembles these rows into the transposed matrix, which is returned as the output of the function.

'''
