# We need a simple function that determines if a plural is needed or not. It should take a number, and return true if a plural should be used with that number or false if not. This would be useful when printing out a string such as 5 minutes, 14 apples, or 1 sun.
# You only need to worry about english grammar rules for this kata, where anything that isn't singular (one of something), it is plural (not one of something).
# All values will be positive integers or floats, or zero.

def plural(n):
    return n != 1

# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.
# Task
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
# Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.
# Examples
# A size 3 diamond:
#  *
# ***
#  *
# ...which would appear as a string of " *\n***\n *\n"
# A size 5 diamond:

#   *
#  ***
# *****
#  ***
#   *
# ...that is:
# "  *\n ***\n*****\n ***\n  *\n"