# In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

# Notes
# The number can be negative already, in which case no change is required.
# Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

def make_negative( number ):
    return (-number if number > 0 else number)

# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

def find_average(numbers):
    sum = 0
    for x in numbers:
        sum += x
    avg = sum / len(numbers)
    return avg

# Kata Task
# I have a cat and a dog.

# I got them at the same time as kitten/puppy. That was humanYears years ago.

# Return their respective ages now as [humanYears,catYears,dogYears]

# NOTES:

# humanYears >= 1
# humanYears are whole numbers only
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that

def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0
    if human_years >= 3:
        catYears += (((human_years-2)*(4))+9+15)
    elif human_years >= 2:
        catYears += (9+15)
    elif human_years >= 1:
        catYears += 15
        
    if human_years >= 3:
        dogYears += (((human_years-2)*(5))+9+15)
    elif human_years >= 2:
        dogYears += (9+15)
    elif human_years >= 1:
        dogYears += 15


    
    respective_age = [human_years, catYears, dogYears]
    return (respective_age)

# Debugging sayHello function
# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!

def say_hello(name):
    return "Hello," + " " + name

# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.
# More generally given parameters:

# p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

# the function nb_year should return n number of entire years needed to get a population greater or equal to p.

# aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)

def nb_year(p0, percent, aug, p):
    n = 0
    while p0 < p:
        p0 = int(p0*(1 + percent/100)) + aug
        n += 1
    return n

# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

def fake_bin(x):
    result = ""
    for y in x:
        if int(y) < 5:
            result += "0"
        else:
            result += '1'
    return result

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

def are_you_playing_banjo(name):
    say_it = ""
    if name[0] == 'R':
        say_it = name + " plays banjo"
    elif name[0] == 'r':
        say_it = name + " plays banjo"
    else:
        say_it = name + " does not play banjo"
    return say_it

# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    x_amt = 0
    o_amt = 0
    for letter in s:
        if letter == 'x':
            x_amt += 1
        if letter == 'X':
            x_amt += 1
        if letter == 'o':
            o_amt += 1
        if letter == 'O':
            o_amt += 1
    if x_amt == o_amt:
        return True
    else:
        return False


# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

def get_grade(s1, s2, s3):
    avg = (s1+s2+s3)/3
    if avg < 60:
        return "F"
    if avg < 70:
        return "D"
    if avg < 80:
        return "C"
    if avg < 90:
        return "B"
    if avg <= 100:
        return "A"