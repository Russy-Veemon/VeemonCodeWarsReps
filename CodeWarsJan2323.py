# In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.
# Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).
# More details about factorial can be found here.

def factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Kids drink toddy.
# Teens drink coke.
# Young adults drink beer.
# Adults drink whisky.
# Make a function that receive age, and return what they drink.
# Rules:
# Children under 14 old.
# Teens under 18 old.
# Young under 21 old.
# Adults have 21 or more.

def people_with_age_drink(age):
    if age >= 21: return 'drink whisky'
    if age >= 18: return 'drink beer'
    if age >= 14: return 'drink coke'
    else: return 'drink toddy'

# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    total = 0
    if arr == []:
        return 0
    for x in arr:
        if x > 0:
            total += x
    return total

# You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.
# You should not remove or add elements from/to the array.

def two_sort(array):
    array.sort()
    answer = array[0]
    return '***'.join(list(answer))