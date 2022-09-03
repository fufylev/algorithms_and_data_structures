# Uses python3

def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def gcd_fast(a, b):
    return a if b == 0 else gcd_fast(b, a % b)


def lcm_fast(a1, b1):
    if a1 == 0 or b1 == 0:
        return 0
    if a1 % b1 == 0 or b1 % a1 == 0:
        return max(a1, b1)

    return a1 * b1 // gcd_fast(a1, b1)


a, b = map(int, input().split())
print(lcm_fast(a, b))
# 226553150 1023473145 => 46374212988031350
