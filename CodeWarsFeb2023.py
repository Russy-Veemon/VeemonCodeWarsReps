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