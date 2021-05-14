# python3

from sys import stdin


def maximum_loot_value_1(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    #assert len(weights) == len(prices)
    #assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    value = 0

    while capacity > 0 and sum(weights) != 0:

        i = 0
        while 0 in weights:
            i = weights.index(0)
            weights.pop(i)
            prices.pop(i)

        index = 0
        for j in range(len(weights)):
            if prices[index] * weights[j] < prices[j] * weights[index]:
                index = j

        w = min(weights[index], capacity)

        value = value + w*prices[index]/weights[index]

        capacity = capacity - w
        weights.pop(index)

    return value


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    #assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    value = 0
    max_index = 0
    priceDensity = []
    for index in range(len(prices)):
        if weights[index] != 0:
            priceDensity.append(prices[index]/(weights[index]))

    while capacity > 0 and sum(weights) != 0:
        max_index = priceDensity.index(max(priceDensity))
        w = min(weights[max_index], capacity)
        value += w * priceDensity[max_index]
        capacity -= w
        weights.pop(max_index)
        #print(priceDensity)
        priceDensity.pop(max_index)

    #print(weights, prices, priceDensity, capacity)
    return value


if __name__ == "__main__":
    #data = list(map(int, stdin.read().split()))
    data = list(map(int, input().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value_1(input_capacity, input_weights, input_prices)
    print("{:.7f}".format(opt_value))

