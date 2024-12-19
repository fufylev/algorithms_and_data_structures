# Use Python3

"""
Money Change Again

As we already know, a natural greedy strategy for the change problem does not work correctly for any set of
denominations. For example, if the available denominations are 1, 3, and 4, the greedy algorithm will change
6 cents using three coins (4 + 1 + 1) while it can be changed using just two coins (3 + 3). Your goal now is
to apply dynamic programming for solving the Money Change Problem for denominations 1, 3, and 4.
Problem Description

Input Format. Integer money.

Output Format. The minimum number of coins with denominations 1, 3, 4 that changes money.

Constraints. 1 ≤ money ≤ 10^3.

Sample 1.
Input:
2
Output:
2
2 = 1 + 1.

Sample 2.
Input:
34
Output:
9
34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4.

"""


from typing import List, Dict

INF = 9999
Type = int
Coins = List[Type]
Memo = Dict[Type, Type]

# Recursive aproach
# def minCoins(C: Coins, T: Type) -> Type:
#     return self.go(C, T)


# def go(C: Coins, T: Type, memo: Memo = {}, ans: Type = INF) -> Type:
#     if T == 0:
#         return 0
#     if T in memo:
#         return memo[T]
#     for coin in C:
#         if 0 <= T - coin:
#             cnt = 1 + self.go(C, T - coin, memo)
#             ans = min(ans, cnt)
#     memo[T] = ans
#     return ans


def minCoins(C: Coins, T: Type) -> Type:
    dp = [INF] * (T + 1)
    dp[0] = 0
    for i in range(T + 1):
        for coin in C:
            if 0 <= i - coin:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[T]


if __name__ == "__main__":
    C = [1, 3, 4]  # (C)oins
    T = int(input())  # (T)arget
    dp_ans = minCoins(C, T)
    print(dp_ans)

"""
money = int(input())
coins = (1, 3, 4)

def change(money, coins):
    min_coins = [float("inf")]*(money + 1)
    min_coins[0] = 0
    for i in range(1, money + 1):
        for coin in coins:
            if i >= coin:
                num_coins = min_coins[i - coin] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins
    return min_coins[money]

print(change(money, coins))
"""
