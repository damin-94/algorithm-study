# 2장 Part 2, 23쪽 - 이진 트리의 링크 표현
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 추가 테스트 
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)

print("루트:", root.data)
print("왼쪽 자식:", root.left.data)
print("오른쪽 자식:", root.right.data)
print("20의 왼쪽 자식:", root.left.left)