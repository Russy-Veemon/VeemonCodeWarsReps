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

# Create a function that accepts a list/array and a number n, and returns a list/array of the first n elements from the list/array.
# If you need help, here's a reference:
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range

def take(arr,n):
    return arr[:n]

# If you can't sleep, just count sheep!!
# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    count = ''
    if n == 0:
        return ''
    elif n > 0:
        for i in range(1, n + 1):
            count += f"{i} sheep..."
    return count

# This program tests the life of an evaporator containing a gas.
# We know the content of the evaporator (content in ml), the percentage of foam or gas lost every day (evap_per_day) and the threshold (threshold) in percentage beyond which the evaporator is no longer useful. All numbers are strictly positive.
# The program reports the nth day (as an integer) on which the evaporator will be out of use.

def evaporator(content, evap_per_day, threshold):
    n = 0
    threshold_ml = (threshold / 100) * content
    while content > threshold_ml:
        n += 1
        content *= (1 - (evap_per_day / 100))
    return n

# The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).

def cockroach_speed(s):
    return int((s*100000)/3600)