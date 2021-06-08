def make_matrix(row, col):
    array = []
    n = 1
    for i in range(row):
        array.append([])
        for j in range(col):
            array[i].append(n)
            n += 1
    return array

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:2d}".format(matrix[i][j]), end = ' ')

        print()