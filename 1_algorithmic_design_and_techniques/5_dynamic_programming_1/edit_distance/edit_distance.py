# Uses python3

"""
Computing the Edit Distance Between Two Strings
Problem Introduction
The edit distance between two strings is the minimum number of operations (insertions, deletions, and
substitutions of symbols) to transform one string into another. It is a measure of similarity of two strings.
Edit distance has applications, for example, in computational biology, natural language processing, and spell
checking. Your goal in this problem is to compute the edit distance between two strings.
Problem Description
Task. The goal of this problem is to implement the algorithm for computing the edit distance between two
strings.

Input Format. Each of the two lines of the input contains a string consisting of lower case latin letters.

Constraints. The length of both strings is at least 1 and at most 100.

Output Format. Output the edit distance between the given two strings.

Sample 1.
Input:
ab
ab
Output:
0

Sample 2.
Input:
short
ports
Output:
3
An alignment of total cost 3:
s h o r t −
− p o r t s

Sample 3.
Input:
editing
distance
Output:
5
An alignment of total cost 5:
e d i − t i n g −
− d i s t a n c e
"""


class Solution:
    def editDistance(self, A: str, B: str) -> int:
        M, N = len(A), len(B)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        dp[0][0] = 0

        for i in range(1, M + 1):
            dp[i][0] = i

        for j in range(1, N + 1):
            dp[0][j] = j

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                cost = 0 if A[i - 1] == B[j - 1] else 1
                dp[i][j] = min(
                    dp[i - 1][j - 1] + cost,
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1,
                )

        return dp[M][N]


if __name__ == "__main__":
    solution = Solution()
    A, B = input(), input()
    ans = solution.editDistance(A, B)
    print(ans)
