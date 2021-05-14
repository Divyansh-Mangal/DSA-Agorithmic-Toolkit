# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    candies = 0

    while n > 0:
        candies+=1

        if (candies+1) < (n-2*candies-1):
            summands.append(candies)
            n = n - candies
        elif candies < n - candies:
            summands.append(candies)
            summands.append(n - candies)
            n = 0
        elif candies > n - candies:
            summands.append(n)
            n = 0

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
