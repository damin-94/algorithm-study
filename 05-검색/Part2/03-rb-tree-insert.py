# 5장 Part2 - 레드블랙 트리 노드 정의
class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RBTree:
    def __init__(self):
        self.root = None

    # 형제 노드 찾기
    def get_sibling(self, node):
        if node == node.parent.left:
            sibling = node.parent.right
        else:
            sibling = node.parent.left

        if sibling is None:
            return Node('NIL', 'B')

        return sibling

    # 5장 Part2 46쪽 - 오른쪽 회전
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

    # 5장 Part2 47쪽 - 왼쪽 회전
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

    # 5장 Part2 48쪽 - 삽입
    def insert(self, value):
        new_node = Node(value, 'R')
        self.root = self._insert(new_node, self.root)
        self.fix_tree(new_node)

    # 5장 Part2 48쪽 - BST 방식으로 삽입
    def _insert(self, node, tree):

        if tree == None and self.root == None:
            return node

        if tree.value < node.value:
            if tree.right == None or tree.right.value == 'NIL':
                tree.right = node
                node.parent = tree
            else:
                self._insert(node, tree.right)
        else:
            if tree.left == None or tree.left.value == 'NIL':
                tree.left = node
                node.parent = tree
            else:
                self._insert(node, tree.left)

        return tree

    # 5장 Part2 49쪽 - 삽입 후 트리 복구
    def fix_tree(self, node):

        while node.parent and node.parent.color == 'R':
            uncle = self.get_sibling(node.parent)

            # Case 1: 삼촌이 RED
            if uncle.color == 'R':
                node.parent.color = 'B'
                uncle.color = 'B'
                node.parent.parent.color = 'R'
                node = node.parent.parent

            else:
                if node.parent == node.parent.parent.left:

                    # Case 2-1
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)

                    # Case 2-2
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotate_right(node.parent.parent)

                else:

                    # Case 2-3
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)

                    # Case 2-4
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotate_left(node.parent.parent)

        self.root.color = 'B'

    # 결과 확인을 위한 중위 순회
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.value, node.color)
            self.inorder(node.right)


# 5장 Part2 50~54쪽 - 실행 예제
t = RBTree()

for value in [99, 88, 62, 67, 43, 55, 4, 7]:
    t.insert(value)

print("루트:", t.root.value, t.root.color)
print("삽입 결과:")
t.inorder(t.root)