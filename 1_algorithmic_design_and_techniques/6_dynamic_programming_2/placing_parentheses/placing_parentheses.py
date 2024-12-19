# Uses python3
import operator

"""
Maximizing the Value of an Arithmetic Expression
Problem Introduction
In this problem, your goal is to add parentheses to a given arithmetic
expression to maximize its value. 
max(5−8+7×4−8+9) =?
Problem Description
Task. Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic
operations using additional parentheses.
Input Format. The only line of the input contains a string 𝑠 of length 2𝑛 + 1 for some 𝑛, with symbols
𝑠0, 𝑠1, . . . , 𝑠2𝑛. Each symbol at an even position of 𝑠 is a digit (that is, an integer from 0 to 9) while
each symbol at an odd position is one of three operations from {+,-,*}.
Constraints. 1 ≤ 𝑛 ≤ 14 (hence the string contains at most 29 symbols).
Output Format. Output the maximum possible value of the given arithmetic expression among different
orders of applying arithmetic operations.

Sample 1.
Input:
1+5
Output:
6

Sample 2.
Input:
5-8+7*4-8+9
Output:
200
200 = (5 − ((8 + 7) × (4 − (8 + 9))))
"""


ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def MinAndMax(i, j, m, M, operation):
    minimum = float("+inf")
    maximum = float("-inf")
    for k in range(i, j):
        a = ops[operation[k - 1]](M[i][k], M[k + 1][j])
        b = ops[operation[k - 1]](M[i][k], m[k + 1][j])
        c = ops[operation[k - 1]](m[i][k], M[k + 1][j])
        d = ops[operation[k - 1]](m[i][k], m[k + 1][j])
        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum


def maxValue(digit):
    n = len(digit)
    m = [[0] * (n + 1) for _ in range(n + 1)]
    M = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        m[i][i] = digit[i - 1]
        M[i][i] = digit[i - 1]
    for s in range(1, n):
        for i in range(1, n + 1 - s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(i, j, m, M, operation)
    return M[1][n]


expression = input()
n = len(expression)
digit = [int(expression[i]) for i in range(0, n + 1, 2)]
operation = [expression[i] for i in range(1, n, 2)]
print(maxValue(digit))
