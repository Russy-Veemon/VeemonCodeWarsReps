# Write a simple regex to validate a username. Allowed characters are:
# lowercase letters,
# numbers,
# underscore
# Length should be between 4 and 16 characters (both included).

import re

def validate_usr(username):
    regex = r"^[a-z0-9_]{4,16}$"
    # Define the expression pattern as a raw string
    return bool(re.match(regex, username))
    # use re.match to check if the username matches the pattern above


# Find the number with the most digits.
# If two numbers in the argument array have the same number of digits, return the first one in the array.

def find_longest(arr):
    max_digits = 0
    max_digits_num = None
    
    for num in arr:
        # Count the number of digits in the current number
        num_digits = len(str(num))
        
        # If the current number has more digits than the previous max, update the max
        if num_digits > max_digits:
            max_digits = num_digits
            max_digits_num = num
            
    return max_digits_num