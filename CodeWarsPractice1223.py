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

# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

def square_digits(num):
    sum = ""
    for x in str(num):
        sum += str(int(x)**2)
    return int(sum)

