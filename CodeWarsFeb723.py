# Challenge:
# Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.
# Example:
# Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].

def flatten_and_sort(array):
    flat_arr = []
    for group in array:
        for x in group:
            flat_arr.append(x)
    return sorted(flat_arr)

# Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.

def include(arr,item):
    if item in arr:
        return True
    else:
        return False