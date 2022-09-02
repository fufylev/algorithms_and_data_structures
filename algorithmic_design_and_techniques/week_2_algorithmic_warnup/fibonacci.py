# Uses python3
def calc_fib(given_number):
    if given_number <= 1:
        return given_number

    return calc_fib(given_number - 1) + calc_fib(given_number - 2)


n = int(input())
print(calc_fib(n))
