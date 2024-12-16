# Uses python3

""""""
"""
Fibonacci Number

Problem Description
Task. Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 45.
Output Format. Output 𝐹𝑛.
"""


# the worst algorithm in terms of time execution
def calc_fib(given_number):
    if given_number <= 1:
        return given_number

    return calc_fib(given_number - 1) + calc_fib(given_number - 2)


def calc_fib_by_array(given_number):
    array = [0] * (given_number + 2)
    array[0] = 0
    array[1] = 1
    for i in range(2, given_number + 1):
        array[i] = array[i - 1] + array[i - 2]
    return array[given_number]


# the fastest one
def _calc_fib_by_permutation(given_number):
    a, b = 0, 1

    if given_number <= 1:
        return given_number

    for i in range(2, given_number + 1):
        b, a = a + b, b

    return b


n = int(input())
print(_calc_fib_by_permutation(n))
