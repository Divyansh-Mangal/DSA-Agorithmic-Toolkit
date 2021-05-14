# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    fib_n = [0,1]

    if n<=1:
        return fib_n[n]

    for num in range (2,n+1):
        fib_n.append(fib_n[num-1]+fib_n[num-2])

    return fib_n[n]


if __name__ == '__main__':
    #input_n = int(input())
    print(fibonacci_number(11))
