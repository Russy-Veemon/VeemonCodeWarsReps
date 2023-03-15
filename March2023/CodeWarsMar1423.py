# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.
# How to take the determinant of a matrix -- it is simplest to start with the smallest cases:
# A 1x1 matrix |a| has determinant a.
# A 2x2 matrix [ [a, b], [c, d] ] or
# |a  b|
# |c  d|
# has determinant: a*d - b*c.
# The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n matrices ofn-1 x n-1 size.
# For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or
# |a b c|  
# |d e f|  
# |g h i|  
# the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs:
# |- - -|
# |- e f|
# |- h i|  
# Note the alternation of signs.
# The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:
# det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)


def determinant(matrix):
    # Get the size of the matrix
    n = len(matrix)
    
    # If the matrix is 1x1, return the only element as the determinant
    if n == 1:
        return matrix[0][0]
    
    # If the matrix is 2x2, return the determinant using the formula
    elif n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    # If the matrix is larger than 2x2, calculate the determinant using the Laplace expansion along the first row
    else:
        det = 0
        
        # Iterate over the elements in the first row
        for j in range(n):
            # Multiply the element by its corresponding minor (determinant of the submatrix obtained by removing the row and column containing that element), with alternating signs
            det += ((-1)**j)*matrix[0][j]*determinant(get_minor(matrix, 0, j))
            
        # Return the determinant
        return det

# Helper function to get the minor matrix for a given element (i,j) of the input matrix
def get_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]
