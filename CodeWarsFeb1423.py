# Create a method sayHello/say_hello/SayHello that takes as input a name, city, and state to welcome a person. Note that name will be an array consisting of one or more values that should be joined together with one space between each, and the length of the name array in test cases will vary.
# Example:
# say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
# This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

def say_hello(name, city, state):
    full_name = ' '.join(name)
    return 'Hello, ' + full_name + '! Welcome to ' + city + ', ' + state + '!' 

# 1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681. The sum of these squares is 84100 which is 290 * 290.
# Task
# Find all integers between m and n (m and n integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.
# We will return an array of subarrays or of tuples (in C an array of Pair) or a string. The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

def list_squared(m, n):
# Define a helper function that takes a number and returns the sum of its squared divisors.
    def get_divisors_sum(num):
        # Initialize the sum of squared divisors to 0.
        divisors_sum = 0
        # Loop through all numbers from 1 to the square root of the given number.
        for i in range(1, int(num ** 0.5) + 1):
            # If the number is divisible by i, add i squared to the sum of squared divisors.
            if num % i == 0:
                divisors_sum += i ** 2
                # If i is not the square root of the number, also add the square of the number divided by i.
                if i != num // i:
                    divisors_sum += (num // i) ** 2
        # Return the sum of squared divisors.
        return divisors_sum

    # Initialize an empty list to store the results.
    result = []
    # Loop through all numbers between m and n.
    for num in range(m, n + 1):
        # Calculate the sum of squared divisors for the current number.
        divisors_sum = get_divisors_sum(num)
        # Check if the sum of squared divisors is a perfect square.
        if int(divisors_sum ** 0.5) ** 2 == divisors_sum:
            # If it is, append the number and its sum of squared divisors to the result list.
            result.append([num, divisors_sum])

    # Return the result list.
    return result