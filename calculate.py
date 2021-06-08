operand = int(input("항의 개수? : "))
cal_exp = list(input("수식 입력: "))

lhs_s = ""
rhs_s = ""

if "+" in cal_exp :
    index = cal_exp.index("+")
    op = "+"
elif "-" in cal_exp :
    index = cal_exp.index("-")
    op = "-"
elif "*" in cal_exp :
    index = cal_exp.index("*")
    op = "*"
elif "/" in cal_exp :
    index = cal_exp.index("/")
    op = "/"

for i in range(0, index) :
    lhs_s += cal_exp[i]
for j in range(index + 1, len(cal_exp)) :
    rhs_s += cal_exp[j]

lhs = int(lhs_s)
rhs = int(rhs_s)

if op == "+" :
    print("{} + {} = {}".format(lhs, rhs, lhs + rhs))
elif op == "-" :
    print("{} - {} = {}".format(lhs, rhs, lhs - rhs))
elif op == "*" :
    print("{} * {} = {}".format(lhs, rhs, lhs * rhs))
elif op == "/" :
    print("{} + {} = {}".format(lhs, rhs, lhs / rhs))