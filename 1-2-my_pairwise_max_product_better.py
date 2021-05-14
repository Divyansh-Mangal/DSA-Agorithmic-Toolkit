#pyhton3
import sys

def check_largest(numbers):
    largest = 0
    for i in numbers:
        if largest<i:
            largest = i
    return largest

def pairwise_max_product(length,numbers):
    #print(f'numbers = {numbers}')
    n = len(numbers)
    num1 = check_largest(numbers)
    #print(f'num1 = {num1}')

    numbers.pop(numbers.index(num1))
    #print(f'numbers = {numbers}')

    num2 = check_largest(numbers)
    #print(f'num2 = {num2}')

    return num1*num2


if __name__=='__main__':
    length = int(input())
    numlist = [int(x) for x in input().split()]
    print(numlist)
    print(pairwise_max_product(length ,numlist))
