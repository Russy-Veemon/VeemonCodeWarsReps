# Given an array of integers your solution should find the smallest integer.
# For example:
# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

def find_smallest_int(arr):
    return min(arr)

# All of the animals are having a feast! Each animal is bringing one dish. There is just one rule: the dish must start and end with the same letters as the animal's name. For example, the great blue heron is bringing garlic naan and the chickadee is bringing chocolate cake.
# Write a function feast that takes the animal's name and dish as arguments and returns true or false to indicate whether the beast is allowed to bring the dish to the feast.
# Assume that beast and dish are always lowercase strings, and that each has at least two letters. beast and dish may contain hyphens and spaces, but these will not appear at the beginning or end of the string. They will not contain numerals.

def feast(beast, dish):
    if beast[0] == dish[0] and beast [-1] == dish[-1]:
        return True
    else:
        return False

# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

def duplicate_encode(word):
    word = word.lower()
    new_string = ''
    for x in word:
        if word.count(x) > 1:
            new_string += ')'
        else:
            new_string += '('
    return new_string

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.
# Example: (Input --> Output)
# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)

# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

def duplicate_count(text):
    text = text.lower()
    total = 0
    for x in set(text):
        if text.count(x) > 1:
            total += 1
    return total

# A child is playing with a ball on the nth floor of a tall building. The height of this floor above ground level, h, is known.
# He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
# His mother looks out of a window 1.5 meters from the ground.
# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
# Three conditions must be met for a valid experiment:
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.
# If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
# Note:
# The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        bounces = 0
        while h > window:
            bounces += 2
            h = h*bounce
        return bounces - 1
    else:
        return -1

# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
# If you want to know more: http://en.wikipedia.org/wiki/DNA
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

def DNA_strand(dna):
    compliment_DNA = ''
    for x in dna:
        if x == 'A':
            compliment_DNA += 'T'
        if x == 'T':
            compliment_DNA += 'A'
        if x == 'C':
            compliment_DNA += 'G'
        if x == 'G':
            compliment_DNA += 'C'
    return compliment_DNA