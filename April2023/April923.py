# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
# Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.
# Before the game begins, players set up the board and place the ships accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just single cell.
# The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.
# This is all you need to solve this kata. If you're interested in more information about the game, visit this link.

def validate_battlefield(field):
    # Count the number of ships of each size
    ship_counts = {4: 1, 3: 2, 2: 3, 1: 4}

    # Check for overlapping or adjacent ships
    for i in range(10):
        for j in range(10):
            if field[i][j] == 1:
                # Check if ship is in a valid position
                if not is_valid_ship(field, i, j):
                    return False
                # Decrease the ship count for the corresponding size
                size = get_ship_size(field, i, j)
                ship_counts[size] -= 1
                if ship_counts[size] < 0:
                    # Too many ships of this size
                    return False

    # Check if all ships have been placed
    return sum(ship_counts.values()) == 0

def is_valid_ship(field, i, j):
    # Check if the ship is a straight line
    if (i > 0 and field[i-1][j] == 1) or (i < 9 and field[i+1][j] == 1):
        # Vertical
        for y in range(max(i-1, 0), min(i+2, 10)):
            if j > 0 and field[y][j-1] == 1:
                return False
            if j < 9 and field[y][j+1] == 1:
                return False
    elif (j > 0 and field[i][j-1] == 1) or (j < 9 and field[i][j+1] == 1):
        # Horizontal
        for x in range(max(j-1, 0), min(j+2, 10)):
            if i > 0 and field[i-1][x] == 1:
                return False
            if i < 9 and field[i+1][x] == 1:
                return False
    else:
        # Submarine (single cell)
        pass
    return True

def get_ship_size(field, i, j):
    # Get the size of the ship starting at (i, j)
    if i > 0 and field[i-1][j] == 1:
        # Vertical
        size = 1
        while i-size >= 0 and field[i-size][j] == 1:
            size += 1
    elif j > 0 and field[i][j-1] == 1:
        # Horizontal
        size = 1
        while j-size >= 0 and field[i][j-size] == 1:
            size += 1
    else:
        # Submarine (single cell)
        size = 1
    return size
