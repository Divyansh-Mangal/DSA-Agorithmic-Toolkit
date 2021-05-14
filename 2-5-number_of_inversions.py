# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


import math


def merge_procedure(A,p,q,r,count):
    L = A[p:q+1:]
    R = A[q+1:r+1:]
    index = p
    while (len(L) != 0 or len(R) != 0):
        if L != [] and R != []:
            if L[0] > R[0]:
                A[index] = R[0]
                R.pop(0)
                count += len(L)
            elif R[0] >= L[0] :
                A[index] = L[0]
                L.pop(0)
        elif R == []:
            A[index] = L[0]
            L.pop(0)
        elif L == []:
            A[index] = R[0]
            R.pop(0)
        index += 1
    return (A, count)

def merge_sort(A,p,r,count):
    if p < r:
        q = math.floor((p+r)/2)
        (A, count) = merge_sort(A,p,q,count)
        (A, count) = merge_sort(A,q+1,r,count)
        (A, count) = merge_procedure(A,p,q,r,count)

    return (A, count)


def compute_inversions(a):
    count = 0
    (A, count) = merge_sort(a, 0, len(a)-1, 0)
    return count


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))


