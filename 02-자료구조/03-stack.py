# Stack 생성
stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Top / Peek
print(stack[-1])

# Pop
data = stack.pop()

print(data)
print(stack)

# Empty 확인
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")

# 2장 33쪽 - pop()과 a[-1] 비교

# PPT 왼쪽
a = [1, 2, 3]
print(a.pop())
print(a)

# PPT 오른쪽
a = [1, 2, 3]
print(a[-1])
print(a)