# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    answer = 1
    for x in arr:
        answer = answer * x
    return answer

# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.
# The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...
# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.
# You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.
# The string has a length greater or equal to one and contains only letters from ato z.
# Examples:
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"
# s="aaaxbbbbyyhwawiwjjjwwm"
# printer_error(s) => "8/22"

def printer_error(s):
    num_of_dups = 0
    length_of_arr = len(s)
    bad_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m']
    for x in s:
        if not x in bad_letters:
            num_of_dups += 1
    return str(num_of_dups) + "/" + str(length_of_arr)

# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"