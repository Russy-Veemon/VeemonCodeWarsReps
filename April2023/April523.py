# Given a number of points on a plane, your task is to find two points with the smallest distance between them in linearithmic O(n log n) time.
# Example
#   1  2  3  4  5  6  7  8  9
# 1  
# 2    . A
# 3                . D
# 4                   . F       
# 5             . C
# 6              
# 7                . E
# 8    . B
# 9                   . G
# For the plane above, the input will be:
# (
#   (2,2), # A
#   (2,8), # B
#   (5,5), # C
#   (6,3), # D
#   (6,7), # E
#   (7,4), # F
#   (7,9)  # G
# )
# => closest pair is: ((6,3),(7,4)) or ((7,4),(6,3))
# (both answers are valid. You can return a list of tuples too)
# The two points that are closest to each other are D and F.
# Expected answer should be an array with both points in any order.
# Goal
# The goal is to come up with a function that can find two closest points for any arbitrary array of points, in a linearithmic time.
# Note: Don't use math.hypot, it's too slow...


def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def brute_force(points):
    n = len(points)
    min_dist = float('inf')
    pair = None
    for i in range(n):
        for j in range(i+1, n):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair

def closest_pair(points):
    n = len(points)
    if n <= 3:
        return brute_force(points)
    mid = n // 2
    left = points[:mid]
    right = points[mid:]
    d_left = closest_pair(left)
    d_right = closest_pair(right)
    d = min(d_left, d_right)
    strip = sorted([p for p in points if abs(p[0]-points[mid][0]) < d], key=lambda x: x[1])
    min_dist = d
    pair = None
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if dist(strip[i], strip[j]) < min_dist:
                min_dist = dist(strip[i], strip[j])
                pair = (strip[i], strip[j])
    return pair if pair else (d_left or d_right)

def find_closest_pair(points):
    sorted_points = sorted(points, key=lambda x: x[0])
    return closest_pair(sorted_points)
