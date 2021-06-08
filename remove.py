a = [1, 2, 3, 4, 5]

# for element in a:
#     print(element)
#     if element == 1:
#         a.remove(element)
# print(a)

# while 2 in a:
#     a.remove(2)
# print(a)

# for element in range(a.count(4)):
#     a.remove(4)
    

for element in a: # 메모리에 저장된 공간에 접근
    if element == 1:
        a = []          # 원본 a는 유지되고 a를 새로운 공간에 복사해서 초기화(원본 a가 메모리에 남는듯)
    print(element)

for element in a:
    if element == 1:
        a.clear()       # (함수사용) 원본에 직접 접근하여 초기화
    print(element)