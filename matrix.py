row = int(input("몇 행? : "))
col = int(input("몇 열? : "))
array = []

n = 1
for i in range(row):
    array.append([])
    for j in range(col):
        array[i].append(n)
        n += 1

for i in range(len(array)):
    for j in range(len(array[i])):
        print("{:2d}".format(array[i][j]), end = ' ')

    print()