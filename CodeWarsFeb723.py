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

# There was a test in your class and you passed it. Congratulations!
# But you're an ambitious person. You want to know if you're better than the average student in your class.
# You receive an array with your peers' test scores. Now calculate the average and compare your score!
# Return True if you're better, else False!
# Note:
# Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)