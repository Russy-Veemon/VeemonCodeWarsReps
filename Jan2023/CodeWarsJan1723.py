# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

def correct(s):
    s = s.replace("5", "S")
    s = s.replace("0", "O")
    s = s.replace("1", "I")
    return s

# Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):
# Example: (Input1, Input2 -->Output)
# "4",  "5" --> "9"
# "34", "5" --> "39"
# "", "" --> "0"
# "2", "" --> "2"
# "-5", "3" --> "-2"

def sum_str(a, b):
    if a == '':
        a += '0'
    if b == "":
        b += '0'
    return str(int(a)+int(b))

# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.
# For example:
# a = 1
# b = 4
# --> [1, 2, 3, 4]

def between(a,b):
    array = []
    for x in range (a, b+1):
        array.append(x)
    return array

# Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    return s.replace('!', "")

# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = weight / (height**2)
    if bmi <= 18.5: 
        return "Underweight"
    if bmi <= 25.0 :
        return "Normal"
    if bmi <= 30.0 :
        return "Overweight"
    if bmi > 30 :
        return "Obese"

# In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.
# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.
# Your function will be tested with pre-made examples as well as random ones.
# If you can, try writing it in one line of code.

def find_difference(a, b):
    return  abs((a[0] * a[1] * a[2]) - (b[0] * b[1] * b[2]))

# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"

def reverse_words(text):
    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.


def is_pangram(s):
    s = s.lower().replace(' ','')
    unique_letters = set(s)
    return set('abcdefghijklmnopqrstuvwxyz').issubset(unique_letters)

# This function should test if the factor is a factor of base.
# Return true if it is a factor or false if it is not.
# About factors
# Factors are numbers you can multiply together to get another number.
# 2 and 3 are factors of 6 because: 2 * 3 = 6
# You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
# You can use the mod operator (%) in most languages to check for a remainder
# For example 2 is not a factor of 7 because: 7 % 2 = 1
# Note: base is a non-negative number, factor is a positive number.

def check_for_factor(base, factor):
    if base % factor != 0:
        return False
    else:
        return True