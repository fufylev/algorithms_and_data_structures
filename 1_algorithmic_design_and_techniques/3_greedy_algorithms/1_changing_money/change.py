# Uses python3
import sys

def get_change(m):
    deno = [1, 5, 10]
    n = len(deno)

    ans = []

    i = n - 1
    while i >= 0:

        # Find denominations
        while m >= deno[i]:
            m -= deno[i]
            ans.append(deno[i])

        i -= 1
    return len(ans)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
