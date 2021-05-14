# python3

from random import randint


def partition3(A,p,r):

    x = A[r]
    a = p-1
    for b in range(p,r):
        if A[b] <= x:
            a+=1
            ex = A[b]
            A[b] = A[a]
            A[a] = ex
    ex = A[a+1]
    A[a+1] = x
    A[r] = ex

    x = A[a+1]
    c = p-1
    for b in range(p,a+1):
        if A[b] < x:
            c += 1
            ex = A[b]
            A[b] = A[c]
            A[c] = ex
    return (c+1, a+1)


def randomized_quick_sort(A, p, r):
    if p >= r:
        return
    k = randint(p, r)
    A[p], A[k] = A[k], A[p]
    if p<r:
        (m1, m2) = partition3(A,p,r)
        randomized_quick_sort(A,p,m1-1)
        randomized_quick_sort(A,m2+1,r)
    return A


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
