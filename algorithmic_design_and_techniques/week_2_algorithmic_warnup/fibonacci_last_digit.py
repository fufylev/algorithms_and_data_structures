# Uses python3

import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit_fast(given_number):
    array = [0] * (given_number + 2)
    array[0] = 0
    array[1] = 1
    for i in range(2, given_number + 1):
        array[i] = (array[i - 1] + array[i - 2]) % 10
    return array[given_number]


n = int(input())
print(get_fibonacci_last_digit_naive(n))
