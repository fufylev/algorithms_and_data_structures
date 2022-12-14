# Uses python3

""""""
"""
Greatest Common Divisor

Problem Description
Task. Given two integers ๐ and ๐, find their greatest common divisor.
Input Format. The two integers ๐, ๐ are given in the same line separated by space.
Constraints. 1 โค ๐, ๐ โค 2 ยท 109.
Output Format. Output GCD(๐, ๐).
"""


def gcd_naive(first, second):
    current_gcd = 1
    for d in range(2, min(first, second) + 1):
        if first % d == 0 and second % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_fast(first, second):
    return first if second == 0 else gcd_fast(second, first % second)


a, b = map(int, input().split())
print(gcd_fast(a, b))
