# Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.
# For example:
# solution([1,2,3,10,5]) # should return [1,2,3,5,10]
# solution(None) # should return []

def solution(nums):
    if nums is None:
        return []
    else:
        nums.sort()
        return nums

# The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).
# If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.
# If
# sz is <= 0 or if str is empty return ""
# sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

def rev_rot(strng, sz):
    if sz <= 0 or not strng or sz > len(strng):
        return ""
    chunks = [strng[i:i+sz] for i in range(0, len(strng), sz)]
    result = ""
    for chunk in chunks:
        if len(chunk) < sz:
            break
        sum_of_cubes = sum([int(c)**3 for c in chunk])
        if sum_of_cubes % 2 == 0:
            result += chunk[::-1]
        else:
            result += chunk[1:] + chunk [0]
    return result