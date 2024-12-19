# python3
import numpy
import pprint as pprint


"""
2 Partitioning Souvenirs

You and two of your friends have just returned back home after visiting various countries. Now you would
like to evenly split all the souvenirs that all three of you bought.

Problem Description

Input Format. The first line contains an integer 𝑛. The second line contains integers 𝑣1, 𝑣2, . . . , 𝑣𝑛 separated
by spaces.

Constraints. 1 ≤ 𝑛 ≤ 20, 1 ≤ 𝑣𝑖 ≤ 30 for all 𝑖.

Output Format. Output 1, if it possible to partition 𝑣1, 𝑣2, . . . , 𝑣𝑛 into three subsets with equal sums, and
0 otherwise.

Sample 1.
Input:
4
3 3 3 3
Output:
0

Sample 2.
Input:
1
30
Output:
0

Sample 3.
Input:
13
1 2 3 4 5 5 7 7 8 10 12 19 25
Output:
1
1 + 3 + 7 + 25 = 2 + 4 + 5 + 7 + 8 + 10 = 5 + 12 + 19.

"""


# Discrete Knapsack problem without repetition
def partitions(W, n, items):
    count = 0
    value = numpy.zeros((W + 1, n + 1))
    for i in range(1, W + 1):
        for j in range(1, n + 1):
            value[i][j] = value[i][j - 1]
            if items[j - 1] <= i:
                temp = value[i - items[j - 1]][j - 1] + items[j - 1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W:
                count += 1

    if count < 3:
        print("0")
    else:
        print("1")


if __name__ == "__main__":
    n = int(input())
    item_weights = [int(i) for i in input().split()]
    total_weight = sum(item_weights)
    if n < 3:
        print("0")
    elif total_weight % 3 != 0:
        print("0")
    else:
        partitions(total_weight // 3, n, item_weights)
