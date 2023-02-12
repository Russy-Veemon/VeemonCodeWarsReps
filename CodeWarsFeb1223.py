# Your task is to sum the differences between consecutive pairs in the array in descending order.
# Example
# [2, 1, 10]  -->  9
# In descending order: [10, 2, 1]
# Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9
# If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust).

def sum_of_differences(arr):
    if len(arr) <= 1:
        return 0
    arr.sort(reverse=True)
    return sum([arr[x] - arr[x+1] for x in range(len(arr)-1)])

# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
    def __init__(self,ball_type='regular'):
        self.ball_type = ball_type

# Input: Array of elements
# ["h","o","l","a"]
# Output: String with comma delimited elements of the array in th same order.
# "h,o,l,a"
# Note: if this seems too simple for you try the next level

def print_array(arr):
    string = ''
    for x in arr:
        string += str(x) +','
    new_string = string[:-1]
    return new_string
    # return ','.join(map(str, arr))
    # best practice commented out above using the map function to increase speed of function

# Complete the function which converts hex number (given as a string) to a decimal number.

def hex_to_dec(s):
    return int(s, 16)