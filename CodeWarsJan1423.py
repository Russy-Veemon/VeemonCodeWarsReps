# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

def greet(name):
    return 'Hello, ' + name + ' how are you doing today?'

# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    fusion = a1 + a2
    return ''.join(sorted(list(set(fusion))))

# Given an array of integers, return a new array with each value doubled.
# For example:
# [1, 2, 3] --> [2, 4, 6]

def maps(a):
    double_me = []
    for x in a:
        double_me.append(x*2)
    return double_me

# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []

def invert(lst):
    new_lst = []
    for x in lst:
        new_lst.append(-x)
    return new_lst

# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"