# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.

def alphabet_position(text):
    alphabet = 'abcdefgjhijklmnopqrstuvwxyz'
    text = text.lower()
    result = ''
    for char in text:
        if char in alphabet:
            result += str(ord(char) - 96) + ' '
    return result.strip()

# Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).
# The Haskell version takes a list of directions with data Direction = North | East | West | South.
# The Clojure version returns nil when the path is reduced to nothing.
# The Rust version takes a slice of enum Direction {North, East, West, South}.
# See more examples in "Sample Tests:"

def dirReduc(arr):
    opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    new_dir = []
    for direction in arr:
        if new_dir and new_dir[-1] == opposite[direction]:
            new_dir.pop()
        else:
            new_dir.append(direction)
    return new_dir