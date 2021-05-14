# python3


def max_pairwise_product(length, numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            if max_product < numbers[first] * numbers[second]:
                max_product = numbers[first] * numbers[second]
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(f'input_n = {input_n}, input_numbers = {input_numbers}')
    print(max_pairwise_product(input_n, input_numbers))
