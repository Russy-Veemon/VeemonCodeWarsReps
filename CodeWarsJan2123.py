# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
# For example, when the input is green, output should be yellow.

def update_light(current):
    if current == 'green':
        return 'yellow'
    if current == 'yellow':
        return 'red'
    if current == 'red':
        return 'green'

# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    result = ''
    for x in s:
        if x.isupper():
            result += " " + x
        else:
            result += x
    return result

# In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]

def reverse_list(l):
    return l[::-1]