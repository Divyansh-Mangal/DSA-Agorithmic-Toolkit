import unittest
from maximum_loot import maximum_loot_value, maximum_loot_value_1
from random import randint


class TestMaximumLoot(unittest.TestCase):
    def test(self):
        for (capacity, weights, prices, answer) in [
            (50, [20, 50, 30], [60, 100, 120], 180.0),
            (10, [30], [500], 500/3),
            (9, [4, 3, 5], [5000, 200, 10], 5204)
        ]:
            self.assertAlmostEqual(
                maximum_loot_value(capacity, weights, prices),
                answer,
                delta=1e-03
            )

    def test_2(self):
        count = 1
        while True:
            n = randint(1,10)
            capacity = randint(0, 2* 10**6)
            weights = []
            prices = []
            for i in range(n):
                weights.append(randint(1, 2* 10**6))
                prices.append(randint(1, 2* 10**6))


            if len(weights) == len(prices):
                print(capacity, weights, prices)
                opt1 = maximum_loot_value(capacity, weights, prices)
                opt2 = maximum_loot_value_1(capacity, weights, prices)
                if maximum_loot_value(capacity, weights, prices) != maximum_loot_value_1(capacity, weights, prices):
                    print(opt1, opt2 )
                    print('Failed')
                    break
            count+=1


if __name__ == '__main__':
    unittest.main()
