n = int(input("몇개의 숫자를 입력하시겠습니까? : "))

num_arr = []
sum = 0
for i in range(n) :
    num_arr.append(int(input("{}번째 숫자 : ".format(i + 1))))
    sum += int(num_arr[i])

print("총합 = {}".format(sum))