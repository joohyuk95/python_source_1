score = int(input("점수를 입력하세요 : "))

if 90 <= score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("{} 학점입니다.".format(grade))