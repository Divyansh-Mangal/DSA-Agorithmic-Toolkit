# python3

def arrows_and_matrix(str1, str2):
    str1 = '0' + str1
    str2 = '0' + str2

    l1 = len(str1)
    l2 = len(str2)

    matrix = []
    arrow = []

    for row in range(l1):
        matrix.append([])
        arrow.append([])

        for col in range(l2):
            if row == 0 and col!=0:
                matrix[row].append(col)
                arrow[row].append(['ins'])
            if col == 0 and row != 0:
                matrix[row].append(row)
                arrow[row].append(['dl'])
            if row == 0 and col == 0:
                matrix[row].append(0)
                arrow[row].append('')

            if row > 0 and col > 0:

                if str1[row] == str2[col]:
                    matrix_rc = matrix[row-1][col-1]
                else:
                    matrix_rc = matrix[row-1][col-1] + 1

                opt = min(matrix[row-1][col]+1, matrix[row][col-1]+1, matrix_rc)

                matrix[row].append(opt)


                arrow[row].append([])
                if matrix_rc == opt:
                    if str1[row] == str2[col]:
                        arrow[row][col].append('m')
                    else:
                        arrow[row][col].append('mm')
                if opt == matrix[row-1][col]+1:
                    arrow[row][col].append('dl')
                if opt == matrix[row][col-1]+1:
                    arrow[row][col].append('ins')

    return (matrix, arrow)


def edit_distance(first_string, second_string):
    str1 = first_string
    str2 = second_string
    (matrix, arrow) = arrows_and_matrix(str1, str2)

    str1 = '0' + str1
    str2 = '0' + str2

    l1 = len(str1)
    l2 = len(str2)

    row = l1 - 1
    col = l2 - 1
    paths = 0
    opt_path = [[],[]]
    while row >= 0 and col >= 0:

        if row == 0 and col == 0:
            row -= 1
            col -= 1
        elif arrow[row][col][0] == 'mm' or arrow[row][col][0] == 'm' :
            opt_path[0].append(str1[row])
            opt_path[1].append(str2[col])
            row -= 1
            col -= 1
        elif arrow[row][col][0] == 'dl':
            opt_path[0].append(str1[row])
            opt_path[1].append('_')
            row -= 1

        elif arrow[row][col][0] == 'ins':
            opt_path[0].append('_')
            opt_path[1].append(str2[col])
            col -= 1

    print('\n')
    for _ in range(len(opt_path)):
        opt_path[_] = opt_path[_][::-1]
        #print(opt_path[_])

    count = 0
    for index in range(len(opt_path[0])):
        if opt_path[0][index] != opt_path[1][index]:
            count += 1

    return count


if __name__ == "__main__":

    print(edit_distance(input(), input()))
