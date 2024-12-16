# Uses python3
from typing import List

"""
Longest Common Subsequence of Two Sequences
Problem Introduction
Compute the length of a longest common subsequence of two sequences.

Problem Description
Task. Given two sequences 𝐴 = (𝑎1, 𝑎2, . . . , 𝑎𝑛) and 𝐵 = (𝑏1, 𝑏2, . . . , 𝑏𝑚), find the length of their longest
common subsequence, i.e., the largest non-negative integer 𝑝 such that there exist indices 1 ≤ 𝑖1 <
𝑖2 < · · · < 𝑖𝑝 ≤ 𝑛 and 1 ≤ 𝑗1 < 𝑗2 < · · · < 𝑗𝑝 ≤ 𝑚, such that 𝑎𝑖1 = 𝑏𝑗1 , . . . , 𝑎𝑖𝑝 = 𝑏𝑗𝑝 .

Input Format. First line: 𝑛. Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛. Third line: 𝑚. Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚.

Constraints. 1 ≤ 𝑛,𝑚 ≤ 100; −10^9 < 𝑎𝑖, 𝑏𝑖 < 10^9.

Output Format. Output 𝑝.

Sample 1.
Input:
3
2 7 5
2
2 5
Output:
2
A common subsequence of length 2 is (2, 5).

Sample 2.
Input:
1
7
4
1 2 3 4
Output:
0
The two sequences do not share elements.

Sample 3.
Input:
4
2 7 8 3
4
5 2 8 7
Output:
2
One common subsequence is (2, 7). Another one is (2, 8).
"""

"""
class RECSolution:
    Memo = Dict[int, int]

    def hash(self, i: int, j: int) -> int:
        return 101 * i + j

    def lcs(self, A: List[int], B: List[int], M: int, N: int, memo: Memo = {}) -> int:
        return self.go(A, B, M - 1, N - 1, memo)

    def go(self, A: List[int], B: List[int], i: int, j: int, memo: Memo) -> int:
        key = self.hash(i, j)
        if i < 0 or j < 0:
            memo[key] = 0
        if key in memo:
            return memo[key]
        if A[i] == B[j]:
            memo[key] = 1 + self.go(A, B, i - 1, j - 1, memo)
        else:
            memo[key] = max(
                self.go(A, B, i - 1, j, memo), self.go(A, B, i, j - 1, memo)
            )
        return memo[key]
"""


class DPSolution:
    def lcs(self, A: List[int], B: List[int], M: int, N: int) -> int:
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[M][N]


if __name__ == "__main__":
    # rec_solution = RECSolution()
    dp_solution = DPSolution()
    M, A = int(input()), list(map(int, input().split()))
    N, B = int(input()), list(map(int, input().split()))
    # ans1 = rec_solution.lcs(A, B, M, N)
    ans2 = dp_solution.lcs(A, B, M, N)
    # assert ans1 == ans2
    print(ans2)
