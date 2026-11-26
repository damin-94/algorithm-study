class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def treeInsert(t, x):
    if t is None:
        return Node(x)

    if x < t.key:
        t.left = treeInsert(t.left, x)
    else:
        t.right = treeInsert(t.right, x)

    return t


# 5장 Part1 20쪽 - 이진 검색 트리 삭제
def treeDelete(t, r, p):
    if r == t:
        t = deleteNode(r)
    elif r == p.left:
        p.left = deleteNode(r)
    else:
        p.right = deleteNode(r)

    return t


# 5장 Part1 20쪽 - 노드 삭제
def deleteNode(r):

    # Case 1: 자식이 없는 경우
    if r.left is None and r.right is None:
        return None

    # Case 2-1: 오른쪽 자식만 있는 경우
    elif r.left is None:
        return r.right

    # Case 2-2: 왼쪽 자식만 있는 경우
    elif r.right is None:
        return r.left

    # Case 3: 자식이 두 개인 경우
    else:
        s = r.right
        parent = r

        # 오른쪽 서브트리의 최소 원소 탐색
        while s.left is not None:
            parent = s
            s = s.left

        r.key = s.key

        if s == r.right:
            r.right = s.right
        else:
            parent.left = s.right

        return r


def inorder(t):
    if t is not None:
        inorder(t.left)
        print(t.key, end=" ")
        inorder(t.right)


# 테스트 코드
t = None

for x in [23, 11, 139, 1, 16, 67, 13, 20, 15]:
    t = treeInsert(t, x)

print("삭제 전:")
inorder(t)
print()

# 노드 11 삭제
r = t.left
p = t
t = treeDelete(t, r, p)

print("11 삭제 후:")
inorder(t)
print()