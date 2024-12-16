# Uses python3
import sys

"""
Organizing a Lottery
Problem Introduction
You are organizing an online lottery. To participate, a person bets on a single
integer. You then draw several ranges of consecutive integers at random.
A participant’s payoff then is proportional to the number of ranges that
contain the participant’s number minus the number of ranges that does not
contain it. You need an efficient algorithm for computing the payoffs for all
participants. A naive way to do this is to simply scan, for all participants, the
list of all ranges. However, you lottery is very popular: you have thousands
of participants and thousands of ranges. For this reason, you cannot afford
a slow naive algorithm.

Problem Description

Task. You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
each point, the number of segments that contain this point.

Input Format. The first line contains two non-negative integers 𝑠 and 𝑝 defining the number of segments
and the number of points on a line, respectively. The next 𝑠 lines contain two integers 𝑎𝑖, 𝑏𝑖 defining
the 𝑖-th segment [𝑎𝑖, 𝑏𝑖]. The next line contains 𝑝 integers defining points 𝑥1, 𝑥2, . . . , 𝑥𝑝.

Constraints. 1 ≤ 𝑠, 𝑝 ≤ 50000; −10^8 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 10^8 for all 0 ≤ 𝑖 < 𝑠; −10^8 ≤ 𝑥𝑗 ≤ 10^8 for all 0 ≤ 𝑗 < 𝑝.

Output Format. Output 𝑝 non-negative integers 𝑘0, 𝑘1, . . . , 𝑘𝑝−1 where 𝑘𝑖 is the number of segments which
contain 𝑥𝑖. More formally,
𝑘𝑖 = |{𝑗 : 𝑎𝑗 ≤ 𝑥𝑖 ≤ 𝑏𝑗}| .

Sample 1.
Input:
2 3
0 5
7 10
1 6 11
Output:
1 0 0
Here, we have two segments and three points. The first point lies only in the first segment while the
remaining two points are outside of all the given segments.
"""


input = sys.stdin.read()
data = list(map(int, input.split()))
s = data[0]
k = data[1]
starts = data[2 : 2 * s + 2 : 2]
ends = data[3 : 2 * s + 2 : 2]
points = data[2 * s + 2 :]

lst = []
for point in points:
    lst.append((point, "p"))
for start in starts:
    lst.append((start, "l"))
for end in ends:
    lst.append((end, "r"))
lst.sort()

counts = []
left = 0
right = 0
for pair in lst:
    if pair[1] == "p":
        counts.append(pair)
        continue
    if pair[1] == "l":
        left += 1
    if pair[1] == "r":
        right += 1
    counts.append((left, right))

dic = {}
l = 0
r = 0
for pair in counts:
    if pair[1] == "p":
        segs = l + right - r - s
        dic[pair[0]] = segs
    else:
        l = pair[0]
        r = pair[1]

for point in points:
    print(dic[point], end=" ")
