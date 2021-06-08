# 자연수를 입력받아서 3진수로 변환하고 변환된 숫자를 역으로 정렬한 후
# 다시 10진수로 변환한 숫자를 반환하는 함수 작성

def solution(n):
    answer = 0
    quotient = []
    remainder = []
    
    while True:
        remainder.append(n % 3)
        n //= 3
        quotient.append(n)

        if quotient[-1] < 3:
            break
    remainder.append(quotient[-1])
    remainder.reverse()
    
    for i in range(len(remainder)):
        answer += remainder[i] * (3 ** i) 

    return answer
    
print(solution(22))