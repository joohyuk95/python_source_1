now_time = input("몇시? : ")
now_time_list = now_time.split(":")

hour = int(now_time_list[0])
minute = int(now_time_list[1])

class_minute = list(range(50 + 1))
class_hour = {}

j = 1
for i in range(9, 17 + 1):
    if i == 12:
        continue

    class_hour[i] = "{}교시".format(j)
    j += 1

if (hour in class_hour) and (minute in class_minute):
    print("{} 입니다.".format(class_hour[hour]))
else:
    print("수업 시간이 아닙니다.")