# Uses python3
import sys
from typing import List

"""
2 Majority Element
Problem Introduction
Majority rule is a decision rule that selects the alternative which has a majority,
that is, more than half the votes.
Given a sequence of elements 𝑎1, 𝑎2, . . . , 𝑎𝑛, you would like to check whether
it contains an element that appears more than 𝑛/2 times. A naive way to do
this is the following.

MajorityElement(𝑎1, 𝑎2, . . . , 𝑎𝑛):
for 𝑖 from 1 to 𝑛:
    currentElement ← 𝑎𝑖
    count ← 0
    for 𝑗 from 1 to 𝑛:
        if 𝑎𝑗 = currentElement:
            count ← count + 1
    if count > 𝑛/2:
        return 𝑎𝑖
return “no majority element”

The running time of this algorithm is quadratic. Your goal is to use the divide-and-conquer technique to
design an 𝑂(𝑛 log 𝑛) algorithm.
Problem Description
Task. The goal in this code problem is to check whether an input sequence contains a majority element.
Input Format. The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.
Constraints. 1 ≤ 𝑛 ≤ 10^5; 0 ≤ 𝑎𝑖 ≤ 10^9 for all 0 ≤ 𝑖 < 𝑛.
Output Format. Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times,
and 0 otherwise.

What To Do
As you might have already guessed, this problem can be solved by the divide-and-conquer algorithm in time
𝑂(𝑛 log 𝑛). Indeed, if a sequence of length 𝑛 contains a majority element, then the same element is also
a majority element for one of its halves. Thus, to solve this problem you first split a given sequence into
halves and make two recursive calls. Do you see how to combine the results of two recursive calls?
It is interesting to note that this problem can also be solved in 𝑂(𝑛) time by a more advanced (non-divide
and conquer) algorithm that just scans the given sequence twice.
"""


def hasMajorityElement(A: List[int], N: int) -> bool:
    candidate = 0
    count = 0
    for x in A:
        if count == 0:
            candidate = x
        count = count + 1 if candidate == x else count - 1

    count = 0
    T = (N // 2) + 1
    for x in A:
        count = count + 1 if candidate == x else count
    return T <= count


def majorityElement(nums: List[int]):
    return majorityElementRecursive(nums, 0, len(nums) - 1)


def majorityElementRecursive(nums: List[int], left: int, right: int):
    # Base case: when the subarray has only one element
    if left == right:
        return nums[left]

    # Divide the array into two halves
    mid = left + (right - left) / 2
    leftMajority = majorityElementRecursive(nums, left, mid)
    rightMajority = majorityElementRecursive(nums, mid + 1, right)
    # If both halves have the same majority element, return it
    if leftMajority == rightMajority:
        return leftMajority
    # Otherwise, count occurrences of leftMajority and rightMajority
    leftCount = countInRange(nums, leftMajority, left, right)
    rightCount = countInRange(nums, rightMajority, left, right)
    # Return the majority element with more occurrences
    return leftMajority if (leftCount > rightCount) else rightMajority


def countInRange(nums: List[int], num: int, left: int, right: int):
    count = 0
    for i in range(left, right):
        if nums[i] == num:
            count = count + 1

    return count


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    ans = majorityElement(A)
    print("1" if ans else "0")
