# Uses python3
from typing import List
from collections import namedtuple

"""
Maximum Value of the Loot 
Problem Introduction.
A thief finds much more loot than his bag can fit. Help him to find the most valuable combination of items assuming that any fraction of a loot item can be put into his bag.

Problem Description
Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
Input Format.
The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the value and the weight of 𝑖-th item, respectively.
 
Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑊 ≤ 2 · 106; 0 ≤ 𝑣𝑖 ≤ 2 · 106, 0 < 𝑤𝑖 ≤ 2 · 106 for all 1 ≤ 𝑖 ≤ 𝑛. All the numbers are integers.
 
Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute
value of the difference between the answer of your program and the optimal value should be at most 10−3.
To ensure this, output your answer with at least four digits after the decimal point (otherwise
your answer, while being computed correctly, can turn out to be wrong because of rounding issues).
"""

Item = namedtuple("Item", "V W")


def comparator(item: Item) -> float:
    return item.V / item.W


class Solution:
    def maxValue(self, items: List[Item], W: int) -> float:
        ans = 0
        items.sort(key=comparator, reverse=True)
        for item in items:
            if W == 0:
                break
            if item.W <= W:
                ans += item.V
                W -= item.W
            else:
                fraction = W / item.W
                ans += fraction * item.V
                W = 0
        return ans


if __name__ == "__main__":
    solution = Solution()
    N, W = map(int, input().split())
    items = []
    for _ in range(N):
        Vi, Wi = map(int, input().split())
        item = Item(Vi, Wi)
        items.append(item)
    ans = solution.maxValue(items, W)
    print("%.10f" % ans)
