# python3
import math

def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def partition3(A, p, r):
    x = A[r]
    a = p-1
    for b in range(p, r):
        if A[b] <= x:
            a += 1
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
    #print(a+1,b,c+1,A)

    return (c+1, a+1)


def Clear_win(A,p,r):
    count = 0
    if p<r:
        (m1, m2) = partition3(A, p, r)
        count = m2-m1+1
        #print(count, A, math.floor((len(A)/2)+1))
        if math.floor((len(A)/2)+1) <= count:
            return 1

        if Clear_win(A, p, m1-1) == 1:
            return 1
        if Clear_win(A, m2+1, r) == 1:
            return 1


    return 0



def majority_element(elements):
    assert len(elements) <= 10 ** 5

    return Clear_win(elements, 0, len(elements)-1)


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
