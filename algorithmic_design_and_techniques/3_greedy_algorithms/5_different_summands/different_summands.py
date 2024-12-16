# Uses python3
from typing import List

"""
Problem Introduction
You are organizing a funny competition for children. As a prize fund you have 𝑛
candies. You would like to use these candies for top 𝑘 places in a competition
with a natural restriction that a higher place gets a larger number of candies.
To make as many children happy as possible, you are going to find the largest
value of 𝑘 for which it is possible.

Problem Description

Task. The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise
distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 != 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.
Input Format. The input consists of a single integer 𝑛.
Constraints. 1 ≤ 𝑛 ≤ 10^9.
Output Format. In the first line, output the maximum number 𝑘 such that 𝑛 can be represented as a sum
of 𝑘 pairwise distinct positive integers. In the second line, output 𝑘 pairwise distinct positive integers
that sum up to 𝑛 (if there are many such representations, output any of them).
"""


class Solution:
    def maxNumPrizes(self, N: int) -> List[int]:
        ans = []
        i = 1
        while i + 1 <= N - i:
            ans.append(i)
            N -= i
            i += 1
        if 0 < N:
            ans.append(N)
        return ans


if __name__ == "__main__":
    solution = Solution()
    N = int(input())
    ans = solution.maxNumPrizes(N)
    print(len(ans))
    for x in ans:
        print(x, end=" ")
