# 5장 Part 1 - 이진 검색 트리 노드 정의
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# 5장 Part 1 10쪽 - 이진 검색 트리의 검색
def treeSearch(t, x):
    # 검색 실패 또는 검색 성공
    if t is None or t.key == x:
        return t

    # 왼쪽 서브트리 검색
    if x < t.key:
        return treeSearch(t.left, x)

    # 오른쪽 서브트리 검색
    else:
        return treeSearch(t.right, x)


# 테스트 코드
t = Node(18)
t.left = Node(7)
t.right = Node(26)

t.left.left = Node(3)
t.left.right = Node(12)

t.right.right = Node(31)
t.right.right.left = Node(27)

x = 12
result = treeSearch(t, x)

if result is not None:
    print("검색 성공:", result.key)
else:
    print("검색 실패")