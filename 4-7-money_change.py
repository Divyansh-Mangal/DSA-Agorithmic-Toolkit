# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    from math import floor

    coins = [10, 5, 1]
    change = []
    number_of_coins = 0

    while money > 0 :
        change_coin = coins[0]
        number_of_coins += floor(money/change_coin)
        money = money%change_coin
        coins.pop(0)

    return number_of_coins



if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
