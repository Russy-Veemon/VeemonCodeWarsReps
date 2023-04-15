# Disclaimer
# If you're not yet familiar with the puzzle called Nonogram, I suggest you to solve 5x5 Nonogram Solver first.
# Task
# Complete the function solve(clues) that solves 15-by-15 Nonogram puzzles.
# Your algorithm has to be clever enough to solve all puzzles in time.
# As in 5x5 Nonogram Solver, the input format will look like this:
# input = tuple(column_clues, row_clues)
# each of (row_clues, column_clues) = tuple(
#   tuple(num_of_ones_in_a_row, ...),
#   ...
# )
# Output
# Output is a 2D-tuple of zeros ans ones, representing the solved grid.
# Example
# Here is the example puzzle in the Sample Test.
# Notes
# Some puzzles may have lines with no cells filled. Most Nonogram games show the clues for such lines as a single zero, but the clue for such a line is represented as a zero-length tuple for the sake of this Kata.

UNKNOWN = -1
ZERO = 0
ONE = 1

def solve(clues):
    # Initialize a 15x15 grid with all cells set to UNKNOWN
    grid = [[UNKNOWN]*15 for _ in range(15)]
    
    # Initialize empty lists for possible solutions for rows and columns
    row_possible = []
    col_possible = []
    
    # Find all possible solutions for rows
    for i in range(15):
        row_clues = clues[1][i]
        solution = [UNKNOWN]*15
        for c in row_clues:
            for j in range(15-c+1):
                # Find all possible positions where the sequence of c ones can be placed
                if all(x == UNKNOWN or x == ZERO for x in solution[j:j+c]):
                    # Update the solution with the new ones
                    solution[j:j+c] = [ONE]*c + [ZERO]*(j+c-15)
            # Add the solution to row_possible
            row_possible.append(solution.copy())
    
    # Find all possible solutions for columns
    for j in range(15):
        col_clues = clues[0][j]
        solution = [UNKNOWN]*15
        for c in col_clues:
            for i in range(15-c+1):
                # Find all possible positions where the sequence of c ones can be placed
                if all(grid[k][j] == UNKNOWN or grid[k][j] == ZERO for k in range(i, i+c)):
                    # Update the solution with the
