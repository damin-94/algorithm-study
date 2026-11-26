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