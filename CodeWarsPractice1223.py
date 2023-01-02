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