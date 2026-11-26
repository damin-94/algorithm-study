# 2장 61~64쪽 - 원형 큐
# count로 빈 상태와 가득 찬 상태를 구별한다.

MAX_QUEUE_SIZE = 4


class CircularQueue:
    def __init__(self):
        self.queue = [None] * MAX_QUEUE_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == MAX_QUEUE_SIZE

    def enqueue(self, data):
        if self.is_full():
            raise IndexError("Queue is full")

        self.rear = (self.rear + 1) % MAX_QUEUE_SIZE
        self.queue[self.rear] = data
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        self.front = (self.front + 1) % MAX_QUEUE_SIZE
        data = self.queue[self.front]
        self.queue[self.front] = None
        self.count -= 1
        return data


# 추가 테스트
q = CircularQueue()
print("처음:", q.front, q.rear, q.count)

for data in [10, 20, 30, 40]:
    q.enqueue(data)

print("가득 찼을 때:", q.front, q.rear, q.count)
print("가득 찼는가?", q.is_full())

while not q.is_empty():
    print("꺼낸 값:", q.dequeue())

print("모두 꺼낸 후:", q.front, q.rear, q.count)