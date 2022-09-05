# Uses python3

""""""
"""
Last Digit of the Sum of Fibonacci Numbers

The goal in this problem is to find the last digit of a sum of the first 𝑛 Fibonacci numbers.
Problem Description
Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 1014.
Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
Hint: Instead of computing this sum in a loop, try to come up with a formula for 𝐹0 + 𝐹1 + 𝐹2 + · · · + 𝐹𝑛. For
this, play with small values of 𝑛. Then, use a solution for the previous problem.
"""

"""
Manual computations:

Number:          0	1	2	3	4	5	6	7	8	9	10
Fib(number):     0	1	1	2	3	5	8	13	21	34	55
SumFiBNums:      0	1	2	4	7	12	20	33	54	88	143
Fib(n) mod 10:   0	1	1	2	3	5	8	3	1	4	5
Sum F(n) mod 10: 0	1	2	4	7	2	0	3	4	8	3
From what I got that: 
1. the sum of nth Fibonacci series = Fib(n+2) - 1
2. the sum of nth Fibonacci series by mod 10 = (F(n+2) % 10) - 1

"""


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum_fast(given_number):

    # The pisano period of module 10 is 60, so we can compute only for the reminder of [given_number] % 60
    computed_number = given_number if given_number <= 60 else given_number % 60

    a, b = 0, 1

    if computed_number <= 1:
        return computed_number

    for i in range(2, computed_number + 1):
        b, a = (a + b) % 10, b

    return b


n = int(input())
last_digit = fibonacci_sum_fast(2 + n)
print(last_digit - 1 if last_digit != 0 else 9)
