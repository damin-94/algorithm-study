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

L.print_forward()       
L.print_backward()      

L.delete(20)
L.print_forward()       

L.delete_first()        
L.delete_last()         
print(L.head, L.tail)   

# 2장 28쪽 - 테스트 코드

L = DoublyLinkedList()

# 삽입 테스트
L.insert_first(20)
L.insert_first(10)
L.insert_last(30)
L.insert_last(40)

print("Forward:")
L.print_forward()

print("Backward:")
L.print_backward()

# 중간 삽입 테스트
L.insert_after(20, 25)

print("After insert:")
L.print_forward()

# 삭제 테스트
L.delete_first()
L.delete_last()
L.delete(25)

print("After delete:")
L.print_forward()

# 탐색 테스트
node = L.search(30)

if node is not None:
    print("Found:", node.data)
else:
    print("Not found")