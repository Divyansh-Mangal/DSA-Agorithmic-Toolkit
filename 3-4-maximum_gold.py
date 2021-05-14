# python3

from sys import stdin


def knapsack_norep(W, wts):
    wts = [(0, 0)] + wts
    value = []
    n = len(wts)

    for i in range(0, n):
        value.append([])
        for wt in range(0, W+1):
            if i == 0 or wt == 0:
                value[i].append(0)
            else:
                value[i].append(value[i-1][wt])
                if wt >= wts[i][0]:
                    val = value[i-1][wt - wts[i][0]] + wts[i][1]
                    if value[i][wt] < val:
                        value[i][wt] = val

    return value[n-1][W]


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    weights = list(zip(weights, weights))
    return knapsack_norep(capacity, weights)


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    #input_capacity, n, *input_weights = list(map(int, input().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
