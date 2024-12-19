# Uses python3
from typing import List, Dict
from pprint import pprint

"""
1 Maximum Amount of Gold
Problem Introduction

You are given a set of bars of gold and your goal is to take as much gold as possible into
your bag. There is just one copy of each bar and for each bar you can either take it or not
(hence you cannot take a fraction of a bar).

Problem Description

Task. Given 𝑛 gold bars, find the maximum weight of gold that fits into a bag of capacity 𝑊.

Input Format. The first line of the input contains the capacity 𝑊 of a knapsack and the number 𝑛 of bars
of gold. The next line contains 𝑛 integers 𝑤0,𝑤1, . . . ,𝑤𝑛−1 defining the weights of the bars of gold.

Constraints. 1 ≤ 𝑊 ≤ 10^4; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤0, . . . ,𝑤𝑛−1 ≤ 10^5.

Output Format. Output the maximum weight of gold that fits into a knapsack of capacity 𝑊.

Sample 1.
Input:
10 3
1 4 8
Output:
9
Here, the sum of the weights of the first and the last bar is equal to 9.

Starter Files
def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

Starter files contain an implementation of the following greedy strategy: scan the list of given bars of gold
and add the current bar if it fits into the current capacity (note that, in this problem, all the items have the
same value per unit of weight, for a simple reasons: they are all made of gold). As you already know from
the lectures, such a greedy move is not safe. You may want to additionally submit a starter file as a solution
to the grading system to ensure that this greedy algorithm indeed might produce a non-optimal result.
"""

"""
Memo = Dict[int, int]


class RECSolution:
    def hash(self, T: int, i: int) -> int:
        return T + 10001 * i

    def maxKnapsack(self, A: List[int], T: int, memo: Memo = {}) -> int:
        N = len(A)
        return self.go(A, T, N - 1, memo)

    def go(self, A: List[int], T: int, i: int, memo: Memo) -> int:
        key = self.hash(T, i)
        if key in memo:
            return memo[key]
        if i < 0:
            memo[i] = 0
            return memo[i]
        w = A[i] + self.go(A, T - A[i], i - 1, memo) if 0 <= T - A[i] else 0
        wo = self.go(A, T, i - 1, memo)
        memo[key] = max(w, wo)  # max( with, without )
        return memo[key]
"""


class DPSolution:
    def maxWeight(self, capacity, items):
        n = len(items)
        T = [[0] * (capacity + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                T[i][w] = T[i - 1][w]
                if w >= items[i - 1]:
                    weight = T[i - 1][w - items[i - 1]] + items[i - 1]
                    if weight > T[i][w]:
                        T[i][w] = weight
        for item in T:
            print(*item)

        return T[n][capacity]

    def maxKnapsack(self, A: List[int], W: int):
        N = len(A)
        dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, W + 1):
                if 0 <= j - A[i - 1]:
                    dp[i][j] = max(
                        A[i - 1] + dp[i - 1][j - A[i - 1]], dp[i - 1][j]
                    )  # max( with, without )
                else:
                    dp[i][j] = dp[i - 1][j]  # without
        for item in dp:
            print(*item)

        return dp[N][W]


if __name__ == "__main__":
    W, N = map(int, input().split())
    A = list(map(int, input().split()))
    # ans1 = RECSolution().maxKnapsack(A, T)
    ans2 = DPSolution().maxWeight(W, A)
    # assert ans1 == ans2
    print(ans2)
