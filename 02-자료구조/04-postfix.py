# 2장 45쪽 - 후위 표기식 계산
def eval(exp):
    s = []

    for ch in exp:
        if ch not in "+-*/":
            value = int(ch)
            s.append(value)
        else:
            op2 = s.pop()
            op1 = s.pop()

            if ch == '+':
                s.append(op1 + op2)
            elif ch == '-':
                s.append(op1 - op2)
            elif ch == '*':
                s.append(op1 * op2)
            elif ch == '/':
                s.append(int(op1 / op2))  # PPT의 C 정수 나눗셈

    return s.pop()


# 추가 테스트 
print(eval("132*-"))
print(eval("82/3-32*+"))