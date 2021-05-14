# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    A = [0,1]
    coins = [[],[1]]

    if money < 2:
        return A[money]

    for num in range(2,money+1):
        minimum = A[num-1]
        action = 1
        prev = num-1

        if num >= 3:
            minimum = min(minimum,A[num-3])
            if minimum == A[num-3]:
                action = 3
                prev = num-3

        if num >= 4:
            minimum = min(minimum,A[num-4])
            if minimum == A[num-4]:
                action = 4
                prev = num-4

        A.append(minimum+1)
        nex = coins[prev] + [action]
        coins.append(nex)

    #print(coins[-1::])
    NumCoin = A[-1::][0]
    return NumCoin


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
