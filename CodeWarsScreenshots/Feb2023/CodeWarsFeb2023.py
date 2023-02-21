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

# Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".
# The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.
# Upper or lower case letter does not matter -- "eNglisH" is also correct.
# Return value as boolean values, true for the string to contains "English", false for it does not.

def sp_eng(sentence): 
    return 'english' in sentence.lower()

# Create a function that converts US dollars (USD) to Chinese Yuan (CNY) . The input is the amount of USD as an integer, and the output should be a string that states the amount of Yuan followed by 'Chinese Yuan'
# Examples (Input -> Output)
# 15  -> '101.25 Chinese Yuan'
# 465 -> '3138.75 Chinese Yuan'
# The conversion rate you should use is 6.75 CNY for every 1 USD. All numbers should be represented as a string with 2 decimal places. (e.g. "21.00" NOT "21.0" or "21")

def usdcny(usd):
    yuan = (usd)*6.75
    return "{:.2f} Chinese Yuan".format(yuan)

# Wolves have been reintroduced to Great Britain. You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the front of the queue which is at the end of the array:
# [sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    7      6      5      4      3            2      1
# If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf in the array.

def warn_the_sheep(queue):
    if queue[-1] == 'wolf':
        return "Pls go away and stop eating my sheep"
#     checking if the animal in queue is a wolf
    else:
        n = queue.index('wolf')
#         the index() method, which returns the index of the first occurrence of the specified value in the list.
        return "Oi! Sheep number {}! You are about to be eaten by a wolf!".format(len(queue)-n-1)
# We calculate the position of the sheep to warn by subtracting the index of the wolf from the length of the queue, and subtracting 1 (since we are at the front of the queue). This gives us the position of the sheep to warn.