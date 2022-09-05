import random

"""
Maximum Pairwise Product
Input format. The first line contains an integer n. The next line contains
n non-negative integers a1; : : : ;an (separated by spaces).
Output format. The maximum pairwise product.
Constraints. 2   n   2   105; 0   a1; : : : ;an   2   105.
"""


def max_pairwise_product_fast(a):
    # n = int(input())
    # a = [int(x) for x in input().split()]
    # assert (len(a) == n)
    index1 = 0
    index2 = 0
    for i in range(1, len(a)):
        if a[i] > a[index1]:
            index1 = i

    if index1 == 0:
        index2 = 1
    else:
        index2 = 0

    for i in range(0, len(a)):
        # if a[i] != a[index1] and a[i] > a[index2]: => cause an error, found by stress test
        if i != index1 and a[i] > a[index2]:
            index2 = i
    print(a[index1] * a[index2])
    print(index1, index2)
    return a[index1] * a[index2]


def max_pairwise_product_naive(a):
    # n = int(input())
    # a = [int(x) for x in input().split()]
    # assert (len(a) == n)
    result = 0

    for i in range(0, len(a)):
        for j in range(i + 1, len(a)):
            if a[i] * a[j] > result:
                result = a[i] * a[j]

    print(result)
    return result


def stress_test(number_of_integers, max_int):
    i = 0
    while i < 100000:
        n = random.randint(2, number_of_integers)
        a = [random.randint(0, max_int) for x in range(n)]
        print(a)
        result1 = max_pairwise_product_naive(a)
        result2 = max_pairwise_product_fast(a)
        if result1 == result2:
            print('OK')
            i += 1
        else:
            print('Wrong answer', result1, result2)
            return


stress_test(100, 100000)
