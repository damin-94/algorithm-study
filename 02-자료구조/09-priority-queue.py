# 2장 66~68쪽 - 연결 리스트로 구현한 우선순위 큐

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        newnode = Node(data)

        # 빈 큐이거나 새 값이 현재 맨 앞 값보다 작은 경우
        if self.front is None or data < self.front.data:
            newnode.next = self.front
            self.front = newnode
            if self.rear is None:
                self.rear = newnode
            return

        # 새 노드가 들어갈 자리의 바로 앞까지 이동
        p = self.front
        while p.next is not None and p.next.data <= data:
            p = p.next

        newnode.next = p.next
        p.next = newnode

        if newnode.next is None:
            self.rear = newnode

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty")

        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def print_queue(self):
        p = self.front
        while p is not None:
            print(p.data, end=" ")
            p = p.next
        print()


# 66~67쪽 - 20 삽입
queue = PriorityQueue()
for data in [2, 17, 22, 23, 56, 117]:
    queue.enqueue(data)

queue.enqueue(20)
print("20 삽입 후:", end=" ")
queue.print_queue()

# 68쪽 - 원래 큐에서 맨 앞 노드 삭제
queue = PriorityQueue()
for data in [2, 17, 22, 23, 56, 117]:
    queue.enqueue(data)

print("꺼낸 값:", queue.dequeue())
print("새 front:", queue.front.data)
print("삭제 후:", end=" ")
queue.print_queue()