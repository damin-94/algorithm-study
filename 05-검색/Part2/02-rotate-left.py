class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.root = None

    # 5장 Part2 47쪽 - Rotate Left
    def rotate_left(self, tree):

        rightchild = tree.right
        tree.right = rightchild.left

        if rightchild.left and rightchild.left.value != 'NIL':
            rightchild.left.parent = tree

        rightchild.parent = tree.parent

        if tree.parent == None:
            self.root = rightchild
        elif tree == tree.parent.left:
            tree.parent.left = rightchild
        else:
            tree.parent.right = rightchild

        rightchild.left = tree
        tree.parent = rightchild


# 5장 Part2 47쪽 - 실행 예제
t = RBTree()

t.root = Node(5)
t.root.left = Node(3)
t.root.right = Node(8)

t.root.left.parent = t.root
t.root.right.parent = t.root

t.root.right.left = Node(6)
t.root.right.right = Node(9)

t.root.right.left.parent = t.root.right
t.root.right.right.parent = t.root.right

print("회전 전 루트:", t.root.value)

t.rotate_left(t.root)

print("회전 후 루트:", t.root.value)
print("왼쪽 자식:", t.root.left.value)
print("오른쪽 자식:", t.root.right.value)
print("왼쪽 자식의 오른쪽 자식:", t.root.left.right.value)