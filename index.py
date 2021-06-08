aa = [3, 4, 5, 6, 7, 8, 4, 4, 3]

index = []
# for i, value in enumerate(aa):
#     if value == 4:
#         index.append(i)
# print(index)


for i in range(len(aa)):
    if aa[i] == 4:
        index.append(i)
print(index)