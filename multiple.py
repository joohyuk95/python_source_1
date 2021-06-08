# 10 미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이며 이들의 총합은 23이다
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라

# 1번
n = int(input("자연수 끝? : " ))

sum = 0
for number in range(1, n):
    if number % 3 == 0 or number % 5 == 0:
        sum += number

print("{} 미만의 자연수 중에서 3과 5의 배수의 총합은 {} 이다.".format(n, sum))

i = 1
sum = 0
while 1<= i < n:
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i += 1
print("{} 미만의 자연수 중에서 3과 5의 배수의 총합은 {} 이다.".format(n, sum))