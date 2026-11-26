# 2장 23~24쪽 - 이중 연결 리스트

# 1. 노드 만들기
class DListNode:
    def __init__(self, data=None):
        self.data = data
        self.llink = None
        self.rlink = None


# 2. 이중 연결 리스트 만들기
class DoublyLinkedList:
    def __init__(self):
        self.head = DListNode()
        self.head.llink = self.head
        self.head.rlink = self.head

    # 23쪽 - before 바로 오른쪽에 새 노드 삽입
    def insert(self, before, data):
        newnode = DListNode(data)

        newnode.llink = before
        newnode.rlink = before.rlink
        before.rlink.llink = newnode
        before.rlink = newnode

        return newnode

    # 24쪽 - 삭제할 노드의 왼쪽 이웃과 오른쪽 이웃을 직접 연결
    def delete(self, removed):
        if removed == self.head:
            return

        removed.llink.rlink = removed.rlink
        removed.rlink.llink = removed.llink

    # 24쪽 - 첫 데이터 노드부터 오른쪽으로 이동하며 출력
    def print_list(self):
        p = self.head.rlink

        while p != self.head:
            print(p.data, end=" ")
            p = p.rlink

        print()


# 3. 테스트 코드
nodes = DoublyLinkedList()

n10 = nodes.insert(nodes.head, 10)
n30 = nodes.insert(n10, 30)
n20 = nodes.insert(n10, 20)  # 10과 30 사이에 20 삽입

print("10의 오른쪽:", n10.rlink.data)
print("30의 왼쪽:", n30.llink.data)

print("삭제 전:", end=" ")
nodes.print_list()

nodes.delete(n20)

print("삭제 후:", end=" ")
nodes.print_list()