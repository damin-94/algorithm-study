# 2장 23쪽 - 이중 연결 리스트 삽입
class DListNode:
    def __init__(self, data=None):
        self.data = data
        self.llink = None
        self.rlink = None


class DoublyLinkedList:
    def __init__(self):
        self.head = DListNode()

        # 비어 있을 때는 head의 양쪽 링크가 자기 자신을 가리킨다.
        self.head.llink = self.head
        self.head.rlink = self.head

    def insert(self, before, data):
        newnode = DListNode(data)

        newnode.llink = before         # 새 노드의 왼쪽은 before
        newnode.rlink = before.rlink   # 새 노드의 오른쪽은 원래 오른쪽 이웃
        before.rlink.llink = newnode   # 오른쪽 이웃의 왼쪽 링크를 새 노드로 변경
        before.rlink = newnode         # before의 오른쪽 링크를 새 노드로 변경

        return newnode

nodes = DoublyLinkedList()
n10 = nodes.insert(nodes.head, 10)
n30 = nodes.insert(n10, 30)
nodes.insert(n10, 20)

print("10의 오른쪽:", n10.rlink.data)
print("30의 왼쪽:", n30.llink.data)