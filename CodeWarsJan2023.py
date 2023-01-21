# Write a function that checks if a given string (case insensitive) is a palindrome.

def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]