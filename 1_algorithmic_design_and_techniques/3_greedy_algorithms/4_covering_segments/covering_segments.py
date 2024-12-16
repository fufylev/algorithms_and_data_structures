# Uses python3

from typing import List

"""
4 Collecting Signatures

Problem Introduction

You are responsible for collecting signatures from all tenants of a certain building.
For each tenant, you know a period of time when he or she is at home.
You would like to collect all signatures by visiting the building as few times as
possible.
The mathematical model for this problem is the following. You are given a set
of segments on a line and your goal is to mark as few points on a line as possible
so that each segment contains at least one marked point.

Problem Description

Task. Given a set of 𝑛 segments {[𝑎0, 𝑏0], [𝑎1, 𝑏1], . . . , [𝑎𝑛−1, 𝑏𝑛−1]} with integer coordinates on a line, find
the minimum number 𝑚 of points such that each segment contains at least one point. That is, find a
set of integers 𝑋 of the minimum size such that for any segment [𝑎𝑖, 𝑏𝑖] there is a point 𝑥 ∈ 𝑋 such
that 𝑎𝑖 ≤ 𝑥 ≤ 𝑏𝑖.

Input Format. The first line of the input contains the number 𝑛 of segments. Each of the following 𝑛 lines
contains two integers 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th
segment.

Constraints. 1 ≤ 𝑛 ≤ 100; 0 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.

Output Format. Output the minimum number 𝑚 of points on the first line and the integer coordinates
of 𝑚 points (separated by spaces) on the second line. You can output the points in any order. If there
are many such sets of points, you can output any set. (It is not difficult to see that there always exist
a set of points of the minimum size such that all the coordinates of the points are integers.)
"""


class Segment:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, rhs):  # descending order of segment end-point b
        if self.b == rhs.b:
            return True if self.a > rhs.a else False
        return True if self.b > rhs.b else False


class Solution:
    def minPoints(self, cur: List[int]):
        ans = []
        cur.sort()
        while 0 < len(cur):
            B = cur[-1].b  # greedy choice: the smallest segment end-point b
            ans.append(B)
            next = []
            for i in range(len(cur)):
                if not (
                    cur[i].a <= B and B <= cur[i].b
                ):  # next is all (s)egments of cur which do NOT contain B
                    next.append(cur[i])
            cur = next
        return ans


if __name__ == "__main__":
    solution = Solution()
    N = int(input())
    S = []
    for _ in range(N):
        a, b = map(int, input().split())
        S.append(Segment(a, b))
    ans = solution.minPoints(S)
    print(len(ans))
    for x in ans:
        print(x, end=" ")
