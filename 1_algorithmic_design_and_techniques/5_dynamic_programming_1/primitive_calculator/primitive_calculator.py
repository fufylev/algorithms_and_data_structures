# Use Python3
from typing import List, Dict

"""
Primitive Calculator
Problem Introduction

You are given a primitive calculator that can perform the following three operations with
the current number 𝑥: multiply 𝑥 by 2, multiply 𝑥 by 3, or add 1 to 𝑥. Your goal is given a
positive integer 𝑛, find the minimum number of operations needed to obtain the number 𝑛
starting from the number 1.

Problem Description

Task. Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛
starting from the number 1.

Input Format. The input consists of a single integer 1 ≤ 𝑛 ≤ 10^6.

Output Format. In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1.

In the second line output a sequence of intermediate numbers. That is, the second line should contain
positive integers 𝑎0, 𝑎2, . . . , 𝑎𝑘−1 such that 𝑎0 = 1, 𝑎𝑘−1 = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, 𝑎𝑖+1 is equal to
either 𝑎𝑖 + 1, 2𝑎𝑖, or 3𝑎𝑖. If there are many such sequences, output any one of them.

Sample 1.
Input:
1
Output:
0
1

Sample 2.
Input:
5
Output:
3
1 2 4 5
Here, we first multiply 1 by 2 two times and then add 1. Another possibility is to first multiply by 3
and then add 1 two times. Hence “1 3 4 5” is also a valid output in this case.

Sample 3.
Input:
96234
Output:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
Again, another valid output in this case is “1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117
96234”.
"""


Type = int
INF = 1000001
Memo = Dict[Type, Type]
Collection = List[Type]


def reconstruct(N: Type, memo: Memo = {}, A: Collection = []) -> Collection:
    while 0 < N:
        A.insert(0, N)
        prev3 = memo[N // 3] if N % 3 == 0 and N // 3 in memo else INF
        prev2 = memo[N // 2] if N % 2 == 0 and N // 2 in memo else INF
        prev1 = memo[N - 1] if N - 1 >= 0 and N - 1 in memo else INF
        prev = min(prev3, prev2, prev1)
        if prev == prev3:
            N //= 3
        elif prev == prev2:
            N //= 2
        elif prev == prev1:
            N -= 1
    return A


class RECSolution:
    def minOps(self, N: Type, memo: Memo = {}) -> Type:
        self.go(N, memo)
        return reconstruct(N, memo)

    def go(self, N: Type, memo: Memo, ans: Type = INF) -> Type:
        if N < 2:
            memo[N] = 0
        if N in memo:
            return memo[N]
        if N % 2 == 0:
            ans = min(ans, 1 + self.go(N // 2, memo))
        if N % 3 == 0:
            ans = min(ans, 1 + self.go(N // 3, memo))
        memo[N] = min(ans, 1 + self.go(N - 1, memo))
        return memo[N]


class DPSolution:
    def minOps(self, N: Type, memo: Memo = {1: 0}) -> Type:
        dp = [INF] * (N + 1)
        dp[1] = 0
        for i in range(2, N + 1):
            if i % 2 == 0:
                dp[i] = min(dp[i], 1 + dp[i // 2])
            if i % 3 == 0:
                dp[i] = min(dp[i], 1 + dp[i // 3])
            memo[i] = dp[i] = min(dp[i], 1 + dp[i - 1])
        return reconstruct(N, memo)


if __name__ == "__main__":
    dp_solution = DPSolution()
    N = int(input())
    A = dp_solution.minOps(N)
    print(len(A) - 1)
    print(A)
    # rec_solution = RECSolution()
    # A1 = rec_solution.minOps(N)
    # assert A1 == A

"""
another way is:

def minOperations(n):
    min_operations = [float("inf")]*(n + 1)
    min_operations[0: 2] = 0, 0
    prev = [0] * (n+1)
    for i in range(2, n + 1):
        if i % 3 != 0:
            temp_3 = float("inf")
        else:
            temp_3 = min_operations[int(i / 3)]
        if i % 2 != 0:
            temp_2 = float("inf")
        else:
            temp_2 = min_operations[int(i / 2)]
        min_operations[i] = min(min_operations[i - 1], temp_2, temp_3) + 1
        if min_operations[i] == temp_3 + 1:
            prev [i] = int(i / 3)
            continue
        if min_operations[i] == temp_2 + 1:
            prev[i] = int(i / 2)
            continue
        if min_operations[i] == min_operations[i - 1] + 1:
            prev[i] = i - 1
    return min_operations, prev


n = int(input())
min_operations, prev = minOperations(n)
result = min_operations[n]
print(result)

sequence = [n]
i = n
while i > 1:
    prev_number = prev[i]
    sequence.append(prev_number)
    i = prev_number
sequence.sort()
for number in sequence:
    print(number, end = ' ')
"""
