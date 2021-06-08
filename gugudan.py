#n = int(input("몇단? : "))

for row in range(1, 9+1):    
    for dan in range(1, 9+1):
        if row == 1:
            print("--- {}단 ---".format(dan), end ='\t')
        else:  
            print("{} x {} = {}".format(dan, row, row*dan), end='\t')
print()