
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# 5장 Part1 15쪽 - 이진 검색 트리 삽입(반복문)
def treeInsert(t, x):
    r = Node(x)

    # 트리가 비어 있는 경우
    if t is None:
        root = r

    else:
        root = t
        p = None
        tmp = t

        # 삽입할 위치 탐색
        while tmp is not None:
            p = tmp

            if x < tmp.key:
                tmp = tmp.left
            else:
                tmp = tmp.right

        # 새로운 노드 삽입
        if x < p.key:
            p.left = r
        else:
            p.right = r

    return root


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