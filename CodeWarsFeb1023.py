# Complete the function which converts a binary number (given as a string) to a decimal number.

def bin_to_decimal(inp):
    dec = 0
    for digit in inp:
        dec = dec * 2 + int(digit)
    return dec