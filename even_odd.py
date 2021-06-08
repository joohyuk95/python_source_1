number = input("정수입력 : ")
last_num = int(number[-1])

even = list(range(0, 10, 2))

if last_num in even:
    print("{} 은(는) 짝수입니다.".format(number))
else:
    print("{} 은(는) 홀수입니다.".format(number))