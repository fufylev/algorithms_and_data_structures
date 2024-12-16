# Use Python3
import math


"""
Finding the Closest Pair of Points

Problem Introduction

In this problem, your goal is to find the closest pair of points among the given 𝑛
points. This is a basic primitive in computational geometry having applications in,
for example, graphics, computer vision, traffic-control systems.

Problem Description
Task. Given 𝑛 points on a plane, find the smallest distance between a pair of two (different) points. Recall
that the distance between points (𝑥1, 𝑦1) and (𝑥2, 𝑦2) is equal to
√︀(𝑥1 − 𝑥2)2 + (𝑦1 − 𝑦2)2.

Input Format. The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point
(𝑥𝑖, 𝑦𝑖).

Constraints. 2 ≤ 𝑛 ≤ 10^5; −10^9 ≤ 𝑥𝑖, 𝑦𝑖 ≤ 10^9 are integers.

Output Format. Output the minimum distance. The absolute value of the difference between the answer
of your program and the optimal value should be at most 10−3. To ensure this, output your answer
with at least four digits after the decimal point (otherwise your answer, while being computed correctly,
can turn out to be wrong because of rounding issues).

What To Do
This computational geometry problem has many applications in computer graphics and vision. A naive
algorithm with quadratic running time iterates through all pairs of points to find the closest pair. Your goal
is to design an 𝑂(𝑛 log 𝑛) time divide and conquer algorithm.
To solve this problem in time 𝑂(𝑛 log 𝑛), let’s first split the given 𝑛 points by an appropriately chosen
vertical line into two halves 𝑆1 and 𝑆2 of size 𝑛
2 (assume for simplicity that all 𝑥-coordinates of the input
points are different). By making two recursive calls for the sets 𝑆1 and 𝑆2, we find the minimum distances
𝑑1 and 𝑑2 in these subsets. Let 𝑑 = min{𝑑1, 𝑑2}.

It remains to check whether there exist points 𝑝1 ∈ 𝑆1 and 𝑝2 ∈ 𝑆2 such that the distance between them
is smaller than 𝑑. We cannot afford to check all possible such pairs since there are 𝑛
2 · 𝑛
2 =  (𝑛2) of them.
To check this faster, we first discard all points from 𝑆1 and 𝑆2 whose 𝑥-distance to the middle line is greater
than 𝑑. That is, we focus on the following strip

Stop and think: Why can we narrow the search to this strip? Now, let’s sort the points of the strip by their
𝑦-coordinates and denote the resulting sorted list by 𝑃 = [𝑝1, . . . , 𝑝𝑘]. It turns out that if |𝑖 − 𝑗| > 7, then
the distance between points 𝑝𝑖 and 𝑝𝑗 is greater than 𝑑 for sure. This follows from the Exercise Break below.
Exercise break: Partition the strip into 𝑑 × 𝑑 squares as shown below and show that each such square
contains at most four input points.

This results in the following algorithm. We first sort the given 𝑛 points by their 𝑥-coordinates and then
split the resulting sorted list into two halves 𝑆1 and 𝑆2 of size 𝑛
2 . By making a recursive call for each of the
sets 𝑆1 and 𝑆2, we find the minimum distances 𝑑1 and 𝑑2 in them. Let 𝑑 = min{𝑑1, 𝑑2}. However, we are not
done yet as we also need to find the minimum distance between points from different sets (i.e, a point from
𝑆1 and a point from 𝑆2) and check whether it is smaller than 𝑑. To perform such a check, we filter the initial
point set and keep only those points whose 𝑥-distance to the middle line does not exceed 𝑑. Afterwards, we
sort the set of points in the resulting strip by their 𝑦-coordinates and scan the resulting list of points. For
each point, we compute its distance to the seven subsequent points in this list and compute 𝑑′, the minimum
distance that we encountered during this scan. Afterwards, we return min{𝑑, 𝑑′}.
The running time of the algorithm satisfies the recurrence relation
𝑇(𝑛) = 2 · 𝑇(︁𝑛2)︁+ 𝑂(𝑛 log 𝑛) .
The 𝑂(𝑛 log 𝑛) term comes from sorting the points in the strip by their 𝑦-coordinates at every iteration.
Exercise break: Prove that 𝑇(𝑛) = 𝑂(𝑛 log2 𝑛) by analyzing the recursion tree of the algorithm.
Exercise break: Show how to bring the running time down to 𝑂(𝑛 log 𝑛) by avoiding sorting at each
recursive call.
"""

n = int(input())
points = []
for i in range(n):
    ipt = input()
    coordinate = tuple(map(int, ipt.split()))
    points.append(coordinate)
points_x_sorted = sorted(points)


def getDistance(point1, point2):
    d = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return d


def bruteForce(points):
    n = len(points)
    d = getDistance(points[0], points[1])
    for i in range(n - 1):
        for j in range(i + 1, n):
            d = min(d, getDistance(points[i], points[j]))
    return d


def stripMin(points_x_sorted, min_d):
    len_p = len(points_x_sorted)
    mid = len_p // 2
    mid_value = points_x_sorted[mid][0]
    points_y_sorted = []
    for point in points_x_sorted:
        if abs(point[0] - mid_value) < min_d:
            points_y_sorted.append(point)
    points_y_sorted.sort(key=lambda p: p[1])
    len_strip = len(points_y_sorted)
    if len_strip < 2:
        return min_d
    else:
        min_d2 = getDistance(points_y_sorted[0], points_y_sorted[1])
        for i in range(len_strip - 1):
            for j in range(i + 1, min(i + 7, len_strip)):
                min_d2 = min(
                    min_d2, getDistance(points_y_sorted[i], points_y_sorted[j])
                )
        return min_d2


def minDistance(points_x_sorted):
    len_p = len(points_x_sorted)
    if len_p <= 3:
        return bruteForce(points_x_sorted)
    else:
        mid = len_p // 2
        min_d_l = minDistance(points_x_sorted[:mid])
        min_d_r = minDistance(points_x_sorted[mid:])
        min_d = min(min_d_l, min_d_r)
        min_d2 = stripMin(points_x_sorted, min_d)
        result = min(min_d, min_d2)
    return result


result = minDistance(points_x_sorted)
print("{0:.9f}".format(result))
