# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    fib_1 = 0
    fib_2 = 1
    fib = 0
    if n<=1:
        return n

    for index in range(2,n+1):
        fib = (fib_1 + fib_2) % 10
        fib_1 = fib_2
        fib_2 = fib
        #last_fib_n.append((last_fib_n[index-1] + last_fib_n[index-2]) % 10)

    return fib


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
