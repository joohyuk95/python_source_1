def add_to_n(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i
    
    print("1부터 {}까지의 총합은 {}입니다.".format(n, total_sum))


def calc(v1, v2, op):
    if op == "+":
        result = v1 + v2
    elif op == "-":
        result = v1 - v2
    elif op == "*":
        result = v1 * v2
    elif op == "/":
        result = v1 / v2
    
    print("{} {} {} = {}".format(v1, op, v2, result))

calc(1, 2, "-")    

number = int(input("총합을 구할 끝 자연수를 입력하시오 : "))
add_to_n(number)
