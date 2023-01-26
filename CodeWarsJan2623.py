# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
# Note: anagrams are case insensitive
# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
# Examples
# "foefet" is an anagram of "toffee"
# "Buckethead" is an anagram of "DeathCubeK"

def is_anagram(test, original):
    # Convert both strings to lowercase
    test = test.lower()
    original = original.lower()
    # Sort the characters of both strings
    test = ''.join(sorted(test))
    original = ''.join(sorted(original))
    # Compare the sorted strings
    return test == original