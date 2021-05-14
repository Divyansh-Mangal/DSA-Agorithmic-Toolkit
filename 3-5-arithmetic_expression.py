# python3

def compute(num1, op, num2):

    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2


def fill_in(m, M, x, y, oplist, numlist):
    if x == y:

        m[y][x] = numlist[x]
        M[y][x] = numlist[x]
    else:
        temp_list = []
        a = y
        b = y+1
        while a < x:

            temp_list.append(compute(m[y][a], oplist[a], m[b][x]))
            temp_list.append(compute(M[y][a], oplist[a], M[b][x]))
            a += 1
            b += 1
        m[y][x] = min(temp_list)
        M[y][x] = max(temp_list)

    return m, M


def maximum(numlist, oplist):
    num = len(numlist)
    m = [['' for i in range(num)] for j in range(num)]
    M = [['' for i in range(num)] for j in range(num)]

    y = 0
    x = 0
    length = 1

    while x <= len(numlist) - 1:

        m, M = fill_in(m, M, x, y, oplist, numlist)

        if x == len(numlist) - 1 and y == 0:
            x += 1
            y += 1
        elif x == len(numlist) - 1:
            x = length
            length += 1
            y = 0
        else:
            x += 1
            y += 1

    return M[0][num-1]


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    numlist = []
    oplist = []
    mylist = dataset
    for index in range(len(mylist)):
        if index % 2 == 0:
            numlist.append(int(mylist[index]))
        elif index % 2 != 0:
            oplist.append(mylist[index])

    return maximum(numlist, oplist)


if __name__ == "__main__":
    print(find_maximum_value(input()))
