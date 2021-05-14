# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def is_better(num, max_num):

    num12 = int(num + max_num)
    num21 = int(max_num + num)

    if num12 > num21:
        return True
    else:
        return False


def largest_number(numbers):

    numbers = list(map(str, numbers))

    salary = []

    while len(numbers) != 0:
        max_num = '0'

        for num in numbers:
            if is_better(num, max_num):
                max_num = num

        salary.append(max_num)
        numbers.pop(numbers.index(max_num))

    my_salary = ''
    for num in salary:
        my_salary += num

    return int(my_salary)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
