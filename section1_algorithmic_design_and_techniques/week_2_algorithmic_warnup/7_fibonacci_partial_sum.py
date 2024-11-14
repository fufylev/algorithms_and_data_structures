# Uses python3
import sys

"""
Last Digit of the Sum of Fibonacci Numbers Again
Problem Introduction
Now, we would like to find the last digit of a partial sum of Fibonacci numbers: 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
Problem Description
Task. Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 +
· · · + 𝐹𝑛.
Input Format. The input consists of two non-negative integers 𝑚 and 𝑛 separated by a space.
Constraints. 0 ≤ 𝑚 ≤ 𝑛 ≤ 10^18.
Output Format. Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
"""


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum_fast(n):
    # The first two Fibonacci numbers
    a, b = 0, 1

    # Base case
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Pisano Period for % 10 is 60
    rem = n % 60

    # Checking the remainder
    if rem == 0:
        return 0

    # The loop will range from 2 to
    # two terms after the remainder
    for i in range(2, rem + 3):
        b, a = (a + b) % 60, b

    s = b - 1
    return s


_from, _to = map(int, input().split())
final = fibonacci_partial_sum_fast(_to) - fibonacci_partial_sum_fast(_from - 1)
print(final % 10)
