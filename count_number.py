# 1부터 1000까지 8이 몇번등장?

goal = input("찾을 숫자 : ")
n = int(input("몇까지? : "))

count = 0
for number in range(1, n + 1):
    str_num = str(number)
    for i in range(len(str_num)):
        if goal == str_num[i]:
            count += 1

print("1부터 {}까지의 자연수 중에서 {}은 총 {}번 등장합니다.".format(n, goal, count))