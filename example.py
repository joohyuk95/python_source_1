numbers = [1123, 44, 22, 1, 32, 48, 133]

isOdd = ""
for number in numbers:
    length = len(str(number))

    if number % 2 :
        isOdd = "홀수"
    else:
        isOdd = "짝수"
    
    print("{} 는 {}이고, {} 자릿수입니다.".format(number, isOdd, length))