# Daily Coding Problem #350

# This problem was asked by Uber.
# Write a program that determines the smallest number of perfect
# squares that sum up to N.

# Thought process: This sounds like a recursion job. Starting with
# the value inputed, we can recursively call the function to see
# if adding the next number down will get value to 0. If not,
# pull out and reduce number by 1. Go until value is 0. Additionally,
# we can see if we've already gone over our current minimum b/c
# going any further would be a waste of time.

import sys


def smallestPerfSqr(n, perf_sqr):
    if n == 0 or n == 1:
        return n
    else:
        result = n
        for p in perf_sqr:
            if n - p >= 0:
                result = min(result, 1 + smallestPerfSqr(n - p, perf_sqr))
            else:
                break
    return result


def minimum_squares(n):
    perf_sqr = []
    for i in range(1, int(n**0.5) + 1):
        if i**2 <= n:
            perf_sqr.append(i**2)
    return smallestPerfSqr(n, perf_sqr)


if __name__ == "__main__":
    value = int(sys.argv[1])
    nperfsqr = minimum_squares(value)
    print(f"Smallest number of perfect squares for {value} : {nperfsqr}")
