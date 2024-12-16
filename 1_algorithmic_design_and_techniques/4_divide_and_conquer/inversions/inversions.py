# Uses python3

from typing import List

"""
Number of Inversions
Problem Introduction

An inversion of a sequence 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 is a pair of indices 0 ≤ 𝑖 < 𝑗 < 𝑛 such
that 𝑎𝑖 > 𝑎𝑗 . The number of inversions of a sequence in some sense measures how
close the sequence is to being sorted. For example, a sorted (in non-descending
order) sequence contains no inversions at all, while in a sequence sorted in descending
order any two elements constitute an inversion (for a total of 𝑛(𝑛 − 1)/2
inversions).

Problem Description
Task. The goal in this problem is to count the number of inversions of a given sequence.
Input Format. The first line contains an integer 𝑛, the next one contains a sequence of integers
𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

Constraints. 1 ≤ 𝑛 ≤ 10^5, 1 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.

Output Format. Output the number of inversions in the sequence.

Sample 1.
Input:
5
2 3 9 2 9
Output:
2
The two inversions here are (1, 3) (𝑎1 = 3 > 2 = 𝑎3) and (2, 3) (𝑎2 = 9 > 2 = 𝑎3).

What To Do
This problem can be solved by modifying the merge sort algorithm. For this, we change both the Merge and
MergeSort procedures as follows:
∙ Merge(𝐵, 𝐶) returns the resulting sorted array and the number of pairs (𝑏, 𝑐) such that 𝑏 ∈ 𝐵, 𝑐 ∈ 𝐶,
and 𝑏 > 𝑐;
∙ MergeSort(𝐴) returns a sorted array 𝐴 and the number of inversions in 𝐴.
"""


Result = List[int], int


class Solution:
    def inversions(self, A: List[int]) -> Result:
        A, cnt = self.go(A, 0, len(A))
        return cnt

    def go(self, A: List[int], L: int, R: int) -> Result:
        size = R - L
        if size < 2:
            return A[L:R], 0
        mid = L + (size // 2)
        A1, cnt1 = self.go(A, L, mid)
        A2, cnt2 = self.go(A, mid, R)
        A3, cnt3 = self.merge(A1, A2)
        return A3, cnt1 + cnt2 + cnt3

    def merge(self, A: List[int], B: List[int]) -> Result:
        C = []
        i = 0
        j = 0
        cnt = 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
                cnt += len(A[i:])
        C.extend(A[i:])
        C.extend(B[j:])
        return C, cnt


if __name__ == "__main__":
    solution = Solution()
    N = input()
    A = list(map(int, input().split()))
    ans = solution.inversions(A)
    print(ans)
