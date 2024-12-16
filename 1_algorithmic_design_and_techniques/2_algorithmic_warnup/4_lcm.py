# Uses python3

""""""
"""
Least Common Multiple
Problem Description
Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.
Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 · 10^9.
Output Format. Output the least common multiple of 𝑎 and 𝑏.
"""


def lcm_naive(first, second):
    for number in range(1, first * second + 1):
        if number % first == 0 and number % second == 0:
            return number

    return first * second


def gcd_fast(first, second):
    return first if second == 0 else gcd_fast(second, first % second)


def lcm_fast(first, second):
    if first == 0 or second == 0:
        return 0
    if first % second == 0 or second % first == 0:
        return max(first, second)

    return first * second // gcd_fast(first, second)


a, b = map(int, input().split())
print(lcm_fast(a, b))
# 226553150 1023473145 => 46374212988031350
