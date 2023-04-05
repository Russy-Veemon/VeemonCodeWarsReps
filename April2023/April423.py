# Your task, is to create a NxN spiral with a given size.
# For example, spiral with size 5 should look like this:
# 00000
# ....0
# 000.0
# 0...0
# 00000
# and with the size 10:
# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000
# Return value should contain array of arrays, of 0 and 1, with the first row being composed of 1s. For example for given size 5 result should be:
# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Because of the edge-cases for tiny spirals, the size will be at least 5.
# General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.

def create_spiral(size):
    # Create empty 2D array filled with zeroes
    spiral = [[0 for j in range(size)] for i in range(size)]

    # Fill in first row with ones
    for j in range(size):
        spiral[0][j] = 1

    # Fill in remaining values in spiral pattern
    i, j = 0, size-1  # Starting position
    num = 2  # Starting number
    while num <= size*size:
        # Move down
        while i+1 < size and spiral[i+1][j] == 0:
            i += 1
            spiral[i][j] = num
            num += 1
        # Move left
        while j-1 >= 0 and spiral[i][j-1] == 0:
            j -= 1
            spiral[i][j] = num
            num += 1
        # Move up
        while i-1 >= 0 and spiral[i-1][j] == 0:
            i -= 1
            spiral[i][j] = num
            num += 1
        # Move right
        while j+1 < size and spiral[i][j+1] == 0:
            j += 1
            spiral[i][j] = num
            num += 1

    # Convert values to ones and zeroes
    for i in range(size):
        for j in range(size):
            spiral[i][j] = 1 if spiral[i][j] == 0 else 0

    return spiral
