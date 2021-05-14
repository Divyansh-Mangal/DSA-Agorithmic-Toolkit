# python3
def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

def pisano_period(m):

    fib_mod = [0,1]

    fib = 0
    fib_1 = 0
    fib_2 = 1
    check = True
    while check:
        fib = fib_1+fib_2
        fib_1 = fib_2
        fib_2 = fib
        fib_mod.append(fib % m)
        if fib_mod[-1] == 1:
            if fib_mod[-2]==0:
                check = False

    fib_mod.pop(-1)
    fib_mod.pop(-1)

    return fib_mod

def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n<=1:
        return n

    pisano = pisano_period(m)
    period = len(pisano)

    return pisano[n%period]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
