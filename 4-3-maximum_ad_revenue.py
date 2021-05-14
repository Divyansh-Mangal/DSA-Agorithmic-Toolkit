# python3

from itertools import permutations


def max_dot_product_naive(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def max_dot_product(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    dot_product = 0

    while first_sequence != []:
        max1 = max(first_sequence)
        max2 = max(second_sequence)
        dot_product += max1 * max2
        first_sequence.pop(first_sequence.index(max1))
        second_sequence.pop(second_sequence.index(max2))

    return dot_product

if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
