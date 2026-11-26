# 5장 Part2 - 노드 정의
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.root = None

    # 5장 Part2 46쪽 - Rotate Right
    def rotate_right(self, tree):

        leftchild = tree.left
        tree.left = leftchild.right

        if leftchild.right and leftchild.right.value != 'NIL':
            leftchild.right.parent = tree

        leftchild.parent = tree.parent

        if tree.parent == None:
            self.root = leftchild
        elif tree == tree.parent.right:
            tree.parent.right = leftchild
        else:
            tree.parent.left = leftchild

        leftchild.right = tree
        tree.parent = leftchild


# 5장 Part2 46쪽 - 실행 예제
t = RBTree()

t.root = Node(8)
t.root.left = Node(5)
t.root.right = Node(9)

t.root.left.parent = t.root
t.root.right.parent = t.root

t.root.left.left = Node(3)
t.root.left.right = Node(6)

t.root.left.left.parent = t.root.left
t.root.left.right.parent = t.root.left

print("회전 전 루트:", t.root.value)

t.rotate_right(t.root)

print("회전 후 루트:", t.root.value)
print("왼쪽 자식:", t.root.left.value)
print("오른쪽 자식:", t.root.right.value)
print("오른쪽 자식의 왼쪽 자식:", t.root.right.left.value)