# Your task is to write function factorial.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

# Define a function that removes duplicates from an array of numbers and returns it as a result.
# The order of the sequence has to stay the same.

def distinct(seq):
    new_seq = []
    for thing in seq:
        if thing not in new_seq:
            new_seq.append(thing)
    return new_seq

# Your goal is to return multiplication table for number that is always an integer from 1 to 10.
# For example, a multiplication table (string) for number == 5 looks like below:
# 1 * 5 = 5
# 2 * 5 = 10
# 3 * 5 = 15
# 4 * 5 = 20
# 5 * 5 = 25
# 6 * 5 = 30
# 7 * 5 = 35
# 8 * 5 = 40
# 9 * 5 = 45
# 10 * 5 = 50
# P. S. You can use \n in string to jump to the next line.
# Note: newlines should be added between rows, but there should be no trailing newline at the end. If you're unsure about the format, look at the sample tests.

def multi_table(number):
    table = ''
    for x in range (1,11):
        table += str(x) +' * ' +str(number) + ' = ' + str(x*number) + '\n'
    return table[:-1]