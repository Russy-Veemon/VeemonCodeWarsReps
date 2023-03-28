# A format for expressing an ordered list of integers is to use a comma separated list of either
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

def format_range(lst):
    n = len(lst)
    if n == 0:
        return ""
    elif n == 1:
        return str(lst[0])
    else:
        ranges = []
        start = lst[0]
        prev = lst[0]
        for i in range(1, n):
            if lst[i] == prev + 1:
                prev = lst[i]
            else:
                if prev - start >= 2:
                    ranges.append(str(start) + "-" + str(prev))
                else:
                    ranges.append(str(start))
                    if prev == start + 1:
                        ranges.append(str(prev))
                start = lst[i]
                prev = lst[i]
        if prev - start >= 2:
            ranges.append(str(start) + "-" + str(prev))
        else:
            ranges.append(str(start))
            if prev == start + 1:
                ranges.append(str(prev))
        return ",".join(ranges)
