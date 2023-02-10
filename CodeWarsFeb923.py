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