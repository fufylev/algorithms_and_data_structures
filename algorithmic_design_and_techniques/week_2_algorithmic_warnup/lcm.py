# Uses python3

# Least Common Multiple
def lcm_naive(first, second):
    for number in range(1, first * second + 1):
        if number % first == 0 and number % second == 0:
            return number

    return first * second


def gcd_fast(first, second):
    return first if second == 0 else gcd_fast(second, first % second)


def lcm_fast(first, second):
    if first == 0 or second == 0:
        return 0
    if first % second == 0 or second % first == 0:
        return max(first, second)

    return first * second // gcd_fast(first, second)


a, b = map(int, input().split())
print(lcm_fast(a, b))
# 226553150 1023473145 => 46374212988031350
