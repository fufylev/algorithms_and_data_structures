# Uses python3

""""""
"""
Last Digit of Fibonacci Number

Problem Description
Task. Given an integer π, find the last digit of the πth Fibonacci number πΉπ (that is, πΉπ mod 10).
Input Format. The input consists of a single integer π.
Constraints. 0 β€ π β€ 107.
Output Format. Output the last digit of πΉπ.
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
