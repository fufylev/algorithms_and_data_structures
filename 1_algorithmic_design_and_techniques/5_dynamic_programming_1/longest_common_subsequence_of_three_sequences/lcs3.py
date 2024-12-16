# Uses python3
from typing import List, Dict

"""
Longest Common Subsequence of Three Sequences
Problem Introduction

Compute the length of a longest common subsequence of three sequences.

Problem Description
Task. Given three sequences 𝐴 = (𝑎1, 𝑎2, . . . , 𝑎𝑛), 𝐵 = (𝑏1, 𝑏2, . . . , 𝑏𝑚), and 𝐶 = (𝑐1, 𝑐2, . . . , 𝑐𝑙), find the
length of their longest common subsequence, i.e., the largest non-negative integer 𝑝 such that there
exist indices 1 ≤ 𝑖1 < 𝑖2 < · · · < 𝑖𝑝 ≤ 𝑛, 1 ≤ 𝑗1 < 𝑗2 < · · · < 𝑗𝑝 ≤ 𝑚, 1 ≤ 𝑘1 < 𝑘2 < · · · < 𝑘𝑝 ≤ 𝑙 such
that 𝑎𝑖1 = 𝑏𝑗1 = 𝑐𝑘1 , . . . , 𝑎𝑖𝑝 = 𝑏𝑗𝑝 = 𝑐𝑘𝑝

Input Format. First line: 𝑛. Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛. Third line: 𝑚. Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚. Fifth line:
𝑙. Sixth line: 𝑐1, 𝑐2, . . . , 𝑐𝑙.

Constraints. 1 ≤ 𝑛, 𝑚, 𝑙 ≤ 100; −10^9 < 𝑎𝑖, 𝑏𝑖, 𝑐𝑖 < 10^9.

Output Format. Output 𝑝.

Sample 1.
Input:
3
1 2 3
3
2 1 3
3
1 3 5
Output:
2
A common subsequence of length 2 is (1, 3).

Sample 2.
Input:
5
8 3 2 1 7
7
8 2 1 3 8 10 7
6
6 8 3 1 4 7
Output:
3
One common subsequence of length 3 in this case is (8, 3, 7). Another one is (8, 1, 7).
7
"""

"""
class RECSolution:
    Memo = Dict[int, int]

    def hash(self, i: int, j: int, k: int) -> int:
        return 101 * 101 * i + 101 * j + k

    def lcs(
        self,
        A: List[int],
        B: List[int],
        C: List[int],
        M: int,
        N: int,
        O: int,
        memo: Memo = {},
    ) -> int:
        return self.go(A, B, C, M - 1, N - 1, O - 1, memo)

    def go(
        self,
        A: List[int],
        B: List[int],
        C: List[int],
        i: int,
        j: int,
        k: int,
        memo: Memo,
    ) -> int:
        key = self.hash(i, j, k)
        if i < 0 or j < 0 or k < 0:
            memo[key] = 0
        if key in memo:
            return memo[key]
        if A[i] == B[j] and A[i] == C[k]:
            memo[key] = 1 + self.go(A, B, C, i - 1, j - 1, k - 1, memo)
        else:
            memo[key] = max(
                self.go(A, B, C, i - 1, j, k, memo),
                self.go(A, B, C, i, j - 1, k, memo),
                self.go(A, B, C, i, j, k - 1, memo),
            )
        return memo[key]
"""


class DPSolution:
    def lcs(
        self, A: List[int], B: List[int], C: List[int], M: int, N: int, Q: int
    ) -> int:
        dp = [[[0 for _ in range(Q + 1)] for _ in range(N + 1)] for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                for k in range(1, Q + 1):
                    if A[i - 1] == B[j - 1] and A[i - 1] == C[k - 1]:
                        dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1]
                    else:
                        dp[i][j][k] = max(
                            dp[i - 1][j][k],
                            dp[i][j - 1][k],
                            dp[i][j][k - 1],
                        )
        return dp[M][N][Q]


if __name__ == "__main__":
    # rec_solution = RECSolution()
    dp_solution = DPSolution()
    M, A = int(input()), list(map(int, input().split()))
    N, B = int(input()), list(map(int, input().split()))
    Q, C = int(input()), list(map(int, input().split()))
    # ans1 = rec_solution.lcs(A, B, C, M, N, O)
    ans2 = dp_solution.lcs(A, B, C, M, N, Q)
    # assert ans1 == ans2
    print(ans2)
