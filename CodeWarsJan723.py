# Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:n, n is the number of hotdogs a customer will buy, different numbers have different prices (refer to the following table), return how much money will the customer spend to buy that number of hotdogs.
# number of hotdogs	price per unit (cents)
# n < 5	100
# n >= 5 and n < 10	95
# n >= 10	90

def sale_hotdogs(n):
    if n < 5:
        return n*100
    elif n >= 5 and n < 10:
        return n*95
    else:
        return n*90

# In this simple exercise, you will build a program that takes a value, integer , and returns a list of its multiples up to another value, limit . If limit is a multiple of integer, it should be included as well. There will only ever be positive integers passed into the function, not consisting of 0. The limit will always be higher than the base.
# For example, if the parameters passed are (2, 6), the function should return [2, 4, 6] as 2, 4, and 6 are the multiples of 2 up to 6

def find_multiples(integer, limit):
    array = []
    add = integer
    while add <=limit :
        array.append(add)
        add += integer
    return array
    
# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

def remove_url_anchor(url):
    final_char = url.find("#")
    if final_char == -1:
        return url
    return url[:final_char]

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

def abbrev_name(name):
    first_name, last_name = name.split()
    first_initial = first_name[0].upper()
    last_initial = last_name[0].upper()
    return f"{first_initial}.{last_initial}"

# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
    if text[-len(ending):] == ending:
        return True
    else:
        return False

# All Star Code Challenge #18
# Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.
# If no occurrences can be found, a count of 0 should be returned.
# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0

def str_count(string, letter):
    count = 0
    for x in string:
        if x == letter:
            count += 1
    return count