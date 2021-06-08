import os

def isdigits(str):
    str_check = str
    str_check[0] = ""
    if str.isdigit():
        return True
    elif str[0] == "-" and str_check.isdigit():
        return True
a = "-1"
b = 3

print(isdigits(a),isdigits(b))

# while (True):    
#     os.system('cls')
    
#     while (True):
#         lhs = input("계산할 첫번째 수를 입력 : ")
#         if isdigits(lhs):
#             lhs = int(lhs)
#             break
#         else:
#             print("정수가 아닙니다.")
#             continue
#     while (True):
#         rhs = input("계산할 두번째 수를 입력 : ")
#         if isdigits(rhs):
#             rhs = int(rhs)
#             break
#         else:
#             print("정수가 아닙니다.")
#             continue
    
#     while (True):
#         op = input("계산할 연산자를 입력 : ")
#         if op == '+' or op == '-' or op == '*' or op == '/':
#             break
#         else:
#             print("연산자가 아닙니다.")
#             continue

#     if op == "+":
#         print("{} + {} = {}".format(lhs, rhs, lhs + rhs))
#     elif op == "-":
#         print("{} - {} = {}".format(lhs, rhs, lhs - rhs))
#     elif op == "*":
#         print("{} * {} = {}".format(lhs, rhs, lhs * rhs))
#     else:
#         print("{} / {} = {}".format(lhs, rhs, lhs / rhs)) 

#     quit = input("\n계속하시겠습니까? [y/n] : ")

#     if quit == "n" or quit == "N":
#         print("프로그램을 종료합니다.\n")
#         break