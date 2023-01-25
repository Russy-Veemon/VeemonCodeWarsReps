# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Write a function get_char() / getChar() which takes a number and returns the corresponding ASCII char for that value.

def get_char(c):
    return chr(c)

# Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

def replace_exclamation(s):
    vowels = 'aeiouAEIOU'
    answer = ''
    for x in s:
        if x in vowels:
            answer +='!'
        else:
            answer += x
    return answer