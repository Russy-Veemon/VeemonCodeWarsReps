# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.
# For example:
# solution([1,2,3,10,5]) # should return [1,2,3,5,10]
# solution(None) # should return []

def solution(nums):
    if nums is None:
        return []
    else:
        nums.sort()
        return nums

# The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).
# If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.
# If
# sz is <= 0 or if str is empty return ""
# sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

def rev_rot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ""
    chunks = [strng[i:i+sz] for i in range(0, len(strng), sz)]
    result = ""
    for chunk in chunks:
        if len(chunk) < sz:
            break
        sum_of_cubes = sum([int(c)**3 for c in chunk])
        if sum_of_cubes % 2 == 0:
            result += chunk[::-1]
        else:
            result += chunk[1:] + chunk [0]
    return result

# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.

def no_boring_zeros(n):
    if n==0:
        return 0
    while n % 10 == 0:
        n = n // 10
    return n

# Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.
# Task
# Your mission:
# Write a function called checkCoupon which verifies that a coupon code is valid and not expired.
# A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code:
        return False
    curr_date = datetime.datetime.strptime(current_date, '%B %d, %Y')
    exp_date = datetime.datetime.strptime(expiration_date, '%B %d, %Y')
    if curr_date > exp_date:
        return False
    return True

# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2
# Input: []
# Output: 0
# Input: [-2.398]
# Output: -2.398
# Assumptions
# You can assume that you are only given numbers.
# You cannot assume the size of the array.
# You can assume that you do get an array and if the array is empty, return 0.

def sum_array(a):
    if a is None:
        return []
    else:
        return sum(a)