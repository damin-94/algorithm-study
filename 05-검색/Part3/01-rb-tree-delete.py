RED = 'R'
BLACK = 'B'


class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.NIL = Node('NIL', BLACK)
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.root = self.NIL

    def rotate_right(self, tree):
        leftchild = tree.left
        tree.left = leftchild.right

        if leftchild.right != self.NIL:
            leftchild.right.parent = tree

        leftchild.parent = tree.parent

        if tree.parent is None:
            self.root = leftchild
        elif tree == tree.parent.right:
            tree.parent.right = leftchild
        else:
            tree.parent.left = leftchild

        leftchild.right = tree
        tree.parent = leftchild

    def rotate_left(self, tree):
        rightchild = tree.right
        tree.right = rightchild.left

        if rightchild.left != self.NIL:
            rightchild.left.parent = tree

        rightchild.parent = tree.parent

        if tree.parent is None:
            self.root = rightchild
        elif tree == tree.parent.left:
            tree.parent.left = rightchild
        else:
            tree.parent.right = rightchild

        rightchild.left = tree
        tree.parent = rightchild

    # 5장 Part3 3~6쪽 - 노드 삭제
    def delete(self, node):

        # 자식이 두 개인 경우
        if node.left != self.NIL and node.right != self.NIL:
            s = node.right

            while s.left != self.NIL:
                s = s.left

            node.value = s.value
            node = s

        color = node.color

        if node.left != self.NIL:
            x = node.left
        else:
            x = node.right

        x.parent = node.parent

        if node.parent is None:
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x

        if color == BLACK:
            self.fix_delete(x)

    # 5장 Part3 13쪽 - 삭제 후 트리 복구
    # x는 흑색마커를 가진 노드
    def fix_delete(self, x):

        while x != self.root and x.color == BLACK:
            parent = x.parent

            if x == parent.left:
                sibling = parent.right

                # Case A: 형제가 RED
                if sibling.color == RED:
                    sibling.color = BLACK
                    parent.color = RED
                    self.rotate_left(parent)
                    sibling = parent.right

                # Case B: 형제의 두 자식이 BLACK
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    x = parent

                else:
                    # Case C: near RED, far BLACK
                    if sibling.right.color == BLACK:
                        sibling.left.color = BLACK
                        sibling.color = RED
                        self.rotate_right(sibling)
                        sibling = parent.right

                    # Case D: far RED
                    sibling.color = parent.color
                    parent.color = BLACK
                    sibling.right.color = BLACK
                    self.rotate_left(parent)
                    x = self.root

            # 흑색마커가 오른쪽에 있는 대칭 상황
            else:
                sibling = parent.left

                # Case A
                if sibling.color == RED:
                    sibling.color = BLACK
                    parent.color = RED
                    self.rotate_right(parent)
                    sibling = parent.left

                # Case B
                if sibling.left.color == BLACK and sibling.right.color == BLACK:
                    sibling.color = RED
                    x = parent

                else:
                    # Case C
                    if sibling.left.color == BLACK:
                        sibling.right.color = BLACK
                        sibling.color = RED
                        self.rotate_left(sibling)
                        sibling = parent.left

                    # Case D
                    sibling.color = parent.color
                    parent.color = BLACK
                    sibling.left.color = BLACK
                    self.rotate_right(parent)
                    x = self.root

        x.color = BLACK

    def inorder(self, node):
        if node != self.NIL:
            self.inorder(node.left)
            print(node.value, node.color)
            self.inorder(node.right)


# Case B 실행 예제
t = RBTree()

A = Node(20, BLACK)
B = Node(10, BLACK)
C = Node(5, RED)
D = Node(30, RED)
E = Node(25, BLACK)
F = Node(35, BLACK)

for node in [A, B, C, D, E, F]:
    node.left = t.NIL
    node.right = t.NIL

t.root = A

A.left = B
A.right = D
B.parent = A
D.parent = A

B.left = C
C.parent = B

D.left = E
D.right = F
E.parent = D
F.parent = D

print("삭제 전:")
t.inorder(t.root)

# BLACK 노드 F 삭제
t.delete(F)

print("35 삭제 후:")
t.inorder(t.root)