# Our football team has finished the championship.
# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.
# For example: ["3:1", "2:2", "0:1", ...]
# Points are awarded for each match as follows:
# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.
# Notes:
# our team always plays 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4

def points(games):
    total_score = 0
    for game in games:
        x, y = map(int, game.split(":"))
        #split splits the string into two parts removing the colon
        #map(int) assing the two strings as integers so that they can be assigned to the variables x, y
        if x > y :
            total_score += 3
        elif x == y :
            total_score += 1
    return total_score

# Given a sequence of numbers, find the largest pair sum in the sequence.
# For example
# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

def largest_pair_sum(numbers): 
    numbers.sort(reverse=True)
    #  sort the numbers from largest to smallest
    return numbers[0] + numbers[1]
    # get the sum of the two largest numbers


# Complete the function which returns the weekday according to the input number:
# 1 returns "Sunday"
# 2 returns "Monday"
# 3 returns "Tuesday"
# 4 returns "Wednesday"
# 5 returns "Thursday"
# 6 returns "Friday"
# 7 returns "Saturday"
# Otherwise returns "Wrong, please enter a number between 1 and 7"

def whatday(day):
    days_of_week = { 
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }
    return days_of_week.get(day, "Wrong, please enter a number between 1 and 7")

# Given an array of positive integers (the weights of the people), return a new array/tuple of two integers, where the first one is the total weight of team 1, and the second one is the total weight of team 2.
# Notes
# Array size is at least 1.

def row_weights(array):
    team1 = 0
    team2 = 0
    for i, weight in enumerate(array):
    # the enumerate function being used in the for loop returns a series of tuples where
    #     each tuple contains an index and a corresponding item from the iterable array
        if i % 2 == 0:
            team1 += weight
        #the modulus is used in the if statement to separate the even and odds
        else:
            team2 += weight
    return (team1, team2)
