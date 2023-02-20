# My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!
# In honor of my grandfather's memory we will write a function using his formula!
# Take a list of ages when each of your great-grandparent died.
# Multiply each number by itself.
# Add them all together.
# Take the square root of the result.
# Divide by two.

import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    all_ages = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    new_arr = []
    for x in all_ages:
        new_arr.append(x*x)
    return int((math.sqrt(sum(new_arr)))/2)

# Given a 2D ( nested ) list ( array, vector, .. ) of size m * n, your task is to find the sum of the minimum values in each row.
# For Example:
# [ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
# , [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
# , [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
# ]
# So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.
# Note: You will always be given a non-empty list containing positive values.
# ENJOYCODING :)

def sum_of_minimums(numbers):
    min_vals = []
    for x in numbers:
        min_vals.append(min(x))
    return sum(min_vals)