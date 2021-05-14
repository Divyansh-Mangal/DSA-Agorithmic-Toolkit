import unittest
from pairwise_max_product_better import pairwise_max_product
from max_pairwise_product import max_pairwise_product
from random import randint

class TestingForPairwiseMaxProduct(unittest.TestCase):
    def testing_all_cases(self):
        numlist = []
        length = randint(2,11)
        for n in range(0,length):
            numlist.append(randint(1,100))
        print(length, numlist)
        solution1 = pairwise_max_product(length,numlist)
        solution2 = max_pairwise_product(length,numlist)
        print(f'solution1 = {solution1}')
        print(f'solution2 = {solution2}')
        #for digit in numlist:
        #self.assertEqual(pairwise_max_product(length,numlist), max_pairwise_product(length,numlist))
        self.assertEqual(solution1, solution2)

if __name__ == '__main__':
    unittest.main()
