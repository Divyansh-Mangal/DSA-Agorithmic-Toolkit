# python3
def LCS_matrix(str1, str2):
    matrix = []

    for x in range(len(str1)):
        matrix.append([])
        for y in range(len(str2)):
            if x==0 or y==0:
                matrix[x].append(0)
            elif str1[x] == str2[y]:
                matrix[x].append(matrix[x-1][y-1]+1)
            else:
                matrix[x].append(max(matrix[x-1][y], matrix[x][y-1]))
    #for _ in range(len(matrix)):
        #print(matrix[_])

    return matrix


def common_str(str1, str2, matrix):
    subseq = []
    x = len(str1) - 1
    y = len(str2) - 1

    while matrix[x][y] != 0:
        if str1[x] == str2[y]:
            subseq.append(str1[x])
            x = x-1
            y = y-1
        else:
            if matrix[x-1][y] >= matrix[x][y-1]:
                x = x-1
            else:
                y = y-1
    seq = []
    for _ in subseq:
        seq = [_] + seq
    return seq

def LCS(str1, str2):
    str1 = [0] + str1
    str2 = [1] + str2

    matrix1 = LCS_matrix(str1, str2)

    strings = common_str(str1, str2, matrix1)

    return strings


    return strings

def lcs3(a, b, c):
    assert len(a) <= 100
    assert len(b) <= 100
    assert len(c) <= 100
    str1 = a
    str2 = b
    str3 = c

    max_len = max(len(LCS(LCS(a,b),c)), len(LCS(LCS(b,a),c)), len(LCS(LCS(c,b),a)), len(LCS(LCS(b,c),a)), len(LCS(LCS(c,a),b)), len(LCS(LCS(a,c),b)))

    return max_len


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
