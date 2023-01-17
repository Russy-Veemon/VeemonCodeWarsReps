# Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:
# "I love you"
# "a little"
# "a lot"
# "passionately"
# "madly"
# "not at all"
# If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.
# When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
# Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.

def how_much_i_love_you(nb_petals):
    petals  = nb_petals % 6
    if petals == 0:
        return 'not at all'
    elif petals == 1:
        return "I love you"
    elif petals == 2:
        return "a little"
    elif petals == 3:
        return "a lot"
    elif petals == 4:
        return "passionately"
    elif petals == 5:
        return "madly"
    elif petals == 6:
        return "not at all"

# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
# For example:
# time = 3 ----> litres = 1
# time = 6.7---> litres = 3
# time = 11.8--> litres = 5

def litres(time):
    water_drank = time * 0.5
    return int(water_drank)

# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
# #Examples:
# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"

def get_middle(s):
    if len(s) % 2 == 0:
        return s[int(len(s)/2)-1:int(len(s)/2)+1]
    else:
        return s[int(len(s)/2)]

# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:
# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
# As usual, your function/method should be pure, i.e. it should not mutate the original string.


def to_alternating_case(string):
    return string.swapcase()
