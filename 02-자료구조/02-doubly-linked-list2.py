# 2장 26쪽 - 기본 틀

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

# 테스트 코드
L = DoublyLinkedList()
print(L.head)
print(L.tail)

# 2장 27쪽 - 이중 연결 리스트 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data):
        # 맨 앞에 새 노드 삽입
        newnode = Node(data)
        newnode.next = self.head

        if self.head is None:
            self.tail = newnode
        else:
            self.head.prev = newnode

        self.head = newnode

    def insert_last(self, data):
        # 맨 뒤에 새 노드 삽입
        newnode = Node(data)
        newnode.prev = self.tail

        if self.tail is None:
            self.head = newnode
        else:
            self.tail.next = newnode

        self.tail = newnode

    def insert_after(self, target, data):
        # target 값을 가진 첫 번째 노드 바로 뒤에 삽입
        p = self.search(target)
        if p is None:
            return

        if p is self.tail:
            self.insert_last(data)
            return

        newnode = Node(data)
        newnode.prev = p
        newnode.next = p.next
        p.next.prev = newnode
        p.next = newnode

    def delete_first(self):
        # 첫 번째 노드 삭제
        if self.head is None:
            return

        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

    def delete_last(self):
        # 마지막 노드 삭제
        if self.tail is None:
            return

        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

    def delete(self, data):
        # data 값을 가진 첫 번째 노드 삭제
        p = self.search(data)
        if p is None:
            return

        if p is self.head:
            self.delete_first()
        elif p is self.tail:
            self.delete_last()
        else:
            p.prev.next = p.next
            p.next.prev = p.prev

    def search(self, data):
        # 앞에서부터 찾아서 해당 노드를 반환
        p = self.head
        while p is not None:
            if p.data == data:
                return p
            p = p.next
        return None

    def print_forward(self):
        # head부터 오른쪽으로 출력
        p = self.head
        while p is not None:
            print(p.data, end=" ")
            p = p.next
        print()

    def print_backward(self):
        # tail부터 왼쪽으로 출력
        p = self.tail
        while p is not None:
            print(p.data, end=" ")
            p = p.prev
        print()


# 테스트 코드
L = DoublyLinkedList()
L.insert_first(10)
L.insert_last(30)
L.insert_after(10, 20)

L.print_forward()       # 10 20 30
L.print_backward()      # 30 20 10

L.delete(20)
L.print_forward()       # 10 30

L.delete_first()        # 10 삭제
L.delete_last()         # 30 삭제
print(L.head, L.tail)   # 빈 리스트 확인