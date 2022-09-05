# Uses python3

# Problem Description
# Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
# Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
# Constraints. 1 ≤ 𝑛 ≤ 1018, 2 ≤ 𝑚 ≤ 105.


def get_fibonacci_huge_naive(first, second):
    if first <= 1:
        return first

    previous = 0
    current = 1

    for _ in range(first - 1):
        previous, current = current, previous + current

    return current % second


def calc_fib_by_permutation(given_number):
    a, b = 0, 1
    if given_number <= 1:
        return n
    for i in range(2, n + 1):
        b, a = a + b, b

    return b


def pisano_length(modulo):
    previous, current = 0, 1
    for i in range(0, modulo * modulo):
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01
        if previous == 0 and current == 1:
            return i + 1


def get_fibonacci_huge_fast(given_number, modulo):
    a, b = 0, 1
    if given_number <= 1:
        return n
    for i in range(2, n + 1):
        b, a = (a + b) % modulo, b

    return b


n, m = map(int, input().split())
remainder = n % pisano_length(m)
print(get_fibonacci_huge_naive(remainder, m))
