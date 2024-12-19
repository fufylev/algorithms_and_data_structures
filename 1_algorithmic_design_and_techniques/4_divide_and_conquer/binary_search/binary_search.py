# Uses python3
from typing import List

"""
1 Binary Search
Problem Introduction
In this problem, you will implement the binary search algorithm that allows searching
very efficiently (even huge) lists, provided that the list is sorted.
Problem Description
Task. The goal in this code problem is to implement the binary search algorithm.
Input Format. The first line of the input contains an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1
of 𝑛 pairwise distinct positive integers in increasing order. The next line contains an integer 𝑘 and 𝑘
positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.
Constraints. 1 ≤ 𝑛, 𝑘 ≤ 10^4; 1 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏𝑗 ≤ 10^9 for all 0 ≤ 𝑗 < 𝑘;
Output Format. For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎𝑗 = 𝑏𝑖 or −1 if there
is no such index.
"""


def binarySearch(A: List[int], T: int) -> List[int]:
    return go(A, T, 0, len(A))


def go(A: List[int], T: int, lo: int, hi: int) -> List[int]:
    if lo == hi:
        return -1
    P = int((lo + hi) / 2)
    if T < A[P]:
        return go(A, T, lo, P)
    if T > A[P]:
        return go(A, T, P + 1, hi)
    return P


if __name__ == "__main__":
    A = list(map(int, input().split()))
    N = A[0]
    A.pop(0)
    T = list(map(int, input().split()))
    M = T[0]
    T.pop(0)
    for i in range(0, M):
        ans = binarySearch(A, T[i])
        print(ans, end=" ")
