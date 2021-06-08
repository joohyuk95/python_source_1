import os
# 생성할 배열의 행과 열을 입력하세요. : 8x7
# x 없으면 재입력
def isthere_x(str1):
    if "x" in str1:
        return True
    else:
        return False

os.system('cls')

while (True):
    check_x = input("생성할 배열의 행과 열을 입력하세요. (행x열): ")
    if isthere_x(check_x):
        matrix_info = check_x.split("x")
        break
    else:
        print("입력 형식이 잘못되었습니다.")
    
matrix = []
value = 1
for row in range(int(matrix_info[0])):
    matrix.append([])
    for col in range(int(matrix_info[1])):
        matrix[row].append(value)
        value += 1

print()
for row in range(len(matrix) + 2):
    for col in range(len(matrix[0]) + 1):
        if row == 0:
            if col == 0:
                print("  |", end="")
            else:
                print("{:2d}".format(col), end=" ")
        elif row == 1:
            print("ㅡ", end=" ")
        else:
            if col == 0:
                print("{} |".format(row-1), end="")
            else:
                print("{:2d}".format(matrix[row-2][col-1]), end=" ")
    print()

print()
while (True):
    check_x = input("출력할 원소의 행과 열을 입력하세요. (행x열) : ")
    
    if isthere_x(check_x):
        print_value = check_x.split("x")
        break
    else:
        print("입력 형식이 잘못되었습니다.")

row = int(print_value[0])
col = int(print_value[1])

print("{}행 {}열의 값은 {}입니다.\n".format(row, col, matrix[row-1][col-1]))
# 출력할 행과 열을 입력하세요 (행x열) : 3x4
# 3행 4열의 값은 10입니다.
