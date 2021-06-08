n, m = map(int, input("").split())

arr = list(map(int, input("").split()))
A = list(map(int, input("").split()))
B = list(map(int, input("").split()))

arr.sort()
A.sort()
B.sort()

same = []
# A, B 중복 값
for i in range(m):
    for j in range(m):
        if A[i] == B[j]:
            same.append(A[i])
            break

# 중복값 제거
for element in same:
    while element in arr:
        arr.remove(element)
    
    A.remove(element)
    B.remove(element)

arr_copy = arr
# 성능 개선
# A, B 중복 삭제 (sorting???)
# A, B의 i번째 원소 둘 중 하나가 
print(A, B, arr, arr_copy)
# 계산
plus = 0
minus = 0

flag_A = 0
flag_B = 0

for element in A:
    print("element:", element)
    for i in range(len(arr)):
        print("i:",i)
        if flag_A == 0 and element == arr[i]:
            flag_A = 1
            plus += 1
            arr_copy.remove(arr[i])
            continue
        elif flag_A == 1 and element == arr[i]:
            plus += 1
            arr_copy.remove(arr[i])
            continue
        elif flag_A == 1 and element != arr[i]:
            flag_A = 0
            break

for element in B:
    for i in range(len(arr_copy)):
        if flag_B == 0 and element == arr_copy[i]:
            flag_B = 1
            minus -= 1
            continue
        elif flag_B == 1 and element == arr_copy[i]:
            minus -= 1
            continue
        elif flag_B == 1 and element != arr_copy[i]:
            flag_B = 0
            break


happiness = plus + minus

print(happiness)