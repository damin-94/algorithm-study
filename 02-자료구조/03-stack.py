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