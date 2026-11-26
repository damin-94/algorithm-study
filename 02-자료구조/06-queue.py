from collections import deque

# Queue 생성
queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print(queue)

# Peek (Front 확인)
print(queue[0])

# Dequeue
data = queue.popleft()
print(data)
print(queue)

# Empty 확인
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")