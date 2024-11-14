# Uses python3

import sys
from typing import List

"""
6 Maximum Salary
Problem Introduction
As the last question of a successful interview, your boss gives you a few pieces of paper
with numbers on it and asks you to compose a largest number from these numbers. The
resulting number is going to be your salary, so you are very much interested in maximizing
this number. How can you do this?
In the lectures, we considered the following algorithm for composing the largest number out of the given
single-digit numbers.

LargestNumber(Digits):
answer ← empty string
while Digits is not empty:
    maxDigit ← −∞
    for digit in Digits:
        if digit ≥ maxDigit:
            maxDigit ← digit
    append maxDigit to answer
    remove maxDigit from Digits
return answer

Unfortunately, this algorithm works only in case the input consists of single-digit numbers. For example, for
an input consisting of two integers 23 and 3 (23 is not a single-digit number!) it returns 233, while the largest
number is in fact 323. In other words, using the largest number from the input as the first number is not a
safe move.
Your goal in this problem is to tweak the above algorithm so that it works not only for single-digit3
numbers, but for arbitrary positive integers.
Problem Description
Task. Compose the largest number out of a set of integers.
Input Format. The first line of the input contains an integer 𝑛. The second line contains integers
𝑎1, 𝑎2, . . . , 𝑎𝑛.
Constraints. 1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑎𝑖 ≤ 10^3 for all 1 ≤ 𝑖 ≤ 𝑛.
Output Format. Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.
"""


def isGreaterOrEqual(digit, maxDigit) -> bool:
    return int(str(digit) + str(maxDigit)) >= int(str(maxDigit) + str(digit))


def largest_number(list: List[int]) -> str:
    res = ""

    while len(list) > 0:
        maxDigit = 0
        for digit in list:
            if isGreaterOrEqual(digit, maxDigit):
                maxDigit = digit
        res = res + str(maxDigit)
        list.remove(maxDigit)
    return res


if __name__ == "__main__":
    N = int(input())
    data = map(int, input().split())
    S = []
    for i in data:
        S.append(i)
    print(largest_number(S))
