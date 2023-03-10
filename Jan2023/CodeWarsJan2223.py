# Create a function finalGrade, which calculates the final grade of a student depending on two parameters: a grade for the exam and a number of completed projects.
# This function should take two arguments: exam - grade for exam (from 0 to 100); projects - number of completed projects (from 0 and above);
# This function should return a number (final grade). There are four types of final grades:
# 100, if a grade for the exam is more than 90 or if a number of completed projects more than 10.
# 90, if a grade for the exam is more than 75 and if a number of completed projects is minimum 5.
# 75, if a grade for the exam is more than 50 and if a number of completed projects is minimum 2.
# 0, in other cases

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0

# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    char_count = {}
    #create a an empty dictionary for key value pairs
    for char in string:
        #iterate through the string
        if char in char_count:
            char_count[char] += 1
        #if the character is already in the dictionary increase the count
        else:
            char_count[char] = 1
        #if the character is not already in the dictionary add it to the dictionary
    return char_count

# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

def increment_string(string):
    if not string:
        return "1"
    #checks if the variable is a string
    if not string[-1].isdigit():
        return string + "1"
    #adding the number 1 to a string with no number at the end
    i = len(string) - 1
    while i >= 0 and string[i].isdigit():
        i -= 1
    #iterates through the string until the the first digit is found in the string
    number = int(string[i+1:]) + 1
    #once the first digit is found add 1 number to it
    leading_zeros = len(string[i+1:]) - len(str(number))
    return string[:i+1] + "0"*leading_zeros + str(number)

# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

def shortcut(string):
    vowels = "aeiou"
    return ''.join([x for x in string if x not in vowels])

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(string):
    words = string.split()
    #split turns the string into a list of words
    return min(len(word) for word in words)
    #we then iterate through that list and find the smalles length word with min

# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
# Write a function which takes a list of strings and returns each line prepended by the correct number.
# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

def number(lines):
    numbered_lines = []
    #create an empty list
    for i, line in enumerate(lines, start=1):
        numbered_lines.append(f"{i}: {line}")
        #iterate through the old list and append to new list proper key value pairs
    return numbered_lines