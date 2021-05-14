# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def pisano_period(m):

    fib_mod = [0, 1]

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
            if fib_mod[-2] == 0:
                check = False

    fib_mod.pop(-1)
    fib_mod.pop(-1)

    return fib_mod


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    pisano = pisano_period(10)
    period = len(pisano)
    return sum(pisano[: (to_index % period)+1:] + pisano[(from_index % period)::]) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
