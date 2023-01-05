# <!-- As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.
# The input to the function will be an array of three distinct numbers (Haskell: a tuple).
# For example:
# gimme([2, 3, 1]) => 0
# 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.
# Another example (just to make sure it is clear):
# gimme([5, 10, 14]) => 1
# 10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1. -->

def gimme(input):
    if input[0] < input[1] and input [0] > input[2]:
        return 0
    if input[0] > input[1] and input [0] < input[2]:
        return 0
    if input[1] < input[0] and input [1] > input[2]:
        return 1
    if input[1] > input[0] and input [1] < input[2]:
        return 1
    if input[2] < input[0] and input [2] > input[1]:
        return 2
    if input[2] > input[0] and input [2] < input[1]:
        return 2


# After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.
# You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.
# Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.
# Write a code that gives out the total amount for different days(d).

def rental_car_cost(d):
    rent = 0
    if d>= 7:
        rent += (40*d) - 50
    elif d >= 3:
        rent += (40*d) - 20
    else:
        rent += 40*d
    return rent

# You are given an odd-length array of integers, in which all of them are the same, except for one single number.
# Complete the method which accepts such an array, and returns that single different number.
# The input array will always be valid! (odd-length >= 3)

def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x