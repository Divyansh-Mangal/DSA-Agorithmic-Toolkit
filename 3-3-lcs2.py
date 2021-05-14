# python3

def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    matrix = []
    str1 = [0] + first_sequence
    str2 = [0] + second_sequence
    for x in range(len(str1)):
        matrix.append([])
        for y in range(len(str2)):
            if x==0 or y==0:
                matrix[x].append(0)
            elif str1[x] == str2[y]:
                matrix[x].append(matrix[x-1][y-1]+1)
            else:
                matrix[x].append(max(matrix[x-1][y], matrix[x][y-1]))


    return matrix[len(str1)-1][len(str2)-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
