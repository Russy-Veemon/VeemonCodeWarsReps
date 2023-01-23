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

# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    if walk.count('s') != walk.count('n') or walk.count('e') != walk.count('w'):
        return False
    else:
        return True

# Overview
# In some scripting languages like PHP, there exists a logical operator (e.g. &&, ||, and, or, etc.) called the "Exclusive Or" (hence the name of this Kata). The exclusive or evaluates two booleans. It then returns true if exactly one of the two expressions are true, false otherwise. For example:
# false xor false == false // since both are false
# true xor false == true // exactly one of the two expressions are true
# false xor true == true // exactly one of the two expressions are true
# true xor true == false // Both are true.  "xor" only returns true if EXACTLY one of the two expressions evaluate to true.
# Task
# Since we cannot define keywords in Javascript (well, at least I don't know how to do it), your task is to define a function xor(a, b) where a and b are the two expressions to be evaluated. Your xor function should have the behaviour described above, returning true if exactly one of the two expressions evaluate to true, false otherwise.

def xor(a,b):
    return a ^ b

# Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
# Examples (input -> output)
# 6, "I"     -> "IIIIII"
# 5, "Hello" -> "HelloHelloHelloHelloHello"

def repeat_str(repeat, string):
    return repeat * string

# You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
# Example (Input --> Output)
# "Hello World" --> "World Hello"
# "Hi There." --> "There. Hi"
# Happy coding!

def reverse(st):
    words = st.split()
    backward = words[::-1]
    return ' '.join([x for x in backward])