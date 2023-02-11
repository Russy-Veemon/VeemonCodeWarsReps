# Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.
# Division by zero should return an empty value.

def remainder(a,b):
    if min(a,b) == 0:
        return None
    elif a > b:
        return a % b
    else: 
        return b % a