# Uses python3

""""""
"""
Last Digit of Fibonacci Number

Problem Description
Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 107.
Output Format. Output the last digit of 𝐹𝑛.
"""


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(given_number):
    a, b = 0, 1

    if given_number <= 1:
        return given_number

    for i in range(2, given_number + 1):
        b, a = (a + b) % 10, b

    return b


number = int(input())

print(get_fibonacci_last_digit_naive(number))
