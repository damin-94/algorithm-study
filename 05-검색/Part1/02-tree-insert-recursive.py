# 5장 Part1 - 이진 검색 트리 노드 정의
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# 5장 Part1 14쪽 - 이진 검색 트리 삽입(재귀)
def treeInsert(t, x):
    # 빈 자리에 새로운 노드 생성
    if t is None:
        r = Node(x)
        return r

    # 왼쪽 서브트리에 삽입
    if x < t.key:
        t.left = treeInsert(t.left, x)
        return t

    # 오른쪽 서브트리에 삽입
    else:
        t.right = treeInsert(t.right, x)
        return t


# 삽입 결과 확인을 위한 중위 순회
def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.key, end=" ")
        inorder(t.right)


# 테스트 코드
t = None

for x in [23, 11, 139, 1, 14, 67, 871]:
    t = treeInsert(t, x)

print("삽입 결과:")
inorder(t)
print()