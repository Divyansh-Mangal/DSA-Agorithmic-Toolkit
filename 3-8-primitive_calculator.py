# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    A = [0,0]
    B = [[1],[1]]

    for num in range(2,n+1):
        minimum  = A[num-1]
        action = 1
        prev = num-1
        if num % 3 == 0:
            if minimum > A[int(num/3)]:
                minimum = A[int(num/3)]
                action  = 3
                prev = int(num/3)
        if num % 2 == 0:
            if minimum > A[int(num/2)]:
                minimum = A[int(num/2)]
                action  = 2
                prev = int(num/2)

        A.append(minimum+1)
        if action == 1:
            nex = B[prev] + [B[prev][-1] + action]
        if action == 2 or action == 3:
            nex = B[prev] + [B[prev][-1] * action]
        B.append(nex)

    return (B[-1])


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
