# 6장 6쪽 - B-Tree 노드 정의
K = 5


class Node:
    def __init__(self, keys=None):
        self.keys = keys if keys is not None else []
        self.children = []
        self.parent = None


# 6장 9쪽 - B-Tree 삽입
def BTreeInsert(t, x):
    r = t

    # 삽입할 리프 노드 탐색
    while r.children:
        i = 0

        while i < len(r.keys) and x > r.keys[i]:
            i += 1

        r = r.children[i]

    # 리프 노드에 키 삽입
    r.keys.append(x)
    r.keys.sort()

    # 오버플로우 발생
    if len(r.keys) > K:
        return clearOverflow(r)

    return t


# 6장 9쪽, 15쪽 - 오버플로우 해결
def clearOverflow(r):
    p = r.parent

    if p is not None:
        i = p.children.index(r)

        # 왼쪽 형제에게 여유가 있는 경우
        if i > 0:
            left = p.children[i - 1]

            if len(left.keys) < K:
                left.keys.append(p.keys[i - 1])
                p.keys[i - 1] = r.keys.pop(0)

                if r.children:
                    child = r.children.pop(0)
                    left.children.append(child)
                    child.parent = left

                return getRoot(p)

        # 오른쪽 형제에게 여유가 있는 경우
        if i < len(p.children) - 1:
            right = p.children[i + 1]

            if len(right.keys) < K:
                right.keys.insert(0, p.keys[i])
                p.keys[i] = r.keys.pop()

                if r.children:
                    child = r.children.pop()
                    right.children.insert(0, child)
                    child.parent = right

                return getRoot(p)

    # 형제에게 여유가 없으면 노드 분할
    mid = len(r.keys) // 2
    middle = r.keys[mid]

    right = Node(r.keys[mid + 1:])
    r.keys = r.keys[:mid]

    if r.children:
        right.children = r.children[mid + 1:]
        r.children = r.children[:mid + 1]

        for child in right.children:
            child.parent = right

    # 루트 노드 분할
    if p is None:
        t = Node([middle])
        t.children = [r, right]

        r.parent = t
        right.parent = t

        return t

    # 가운데 키를 부모 노드로 이동
    i = p.children.index(r)
    p.keys.insert(i, middle)
    p.children.insert(i + 1, right)
    right.parent = p

    # 부모 노드의 오버플로우 확인
    if len(p.keys) > K:
        return clearOverflow(p)

    return getRoot(p)


# 루트 노드 찾기
def getRoot(r):
    while r.parent is not None:
        r = r.parent

    return r


# 트리 출력
def printTree(t, level=0):
    print("    " * level, t.keys)

    for child in t.children:
        printTree(child, level + 1)


# 6장 10쪽 - 초기 B-Tree 구성
t = Node([7, 13, 25, 34])

t.children = [
    Node([1, 2, 3, 4, 6]),
    Node([8, 10]),
    Node([15, 17, 19, 20]),
    Node([27, 28, 30, 33]),
    Node([37, 38, 40, 41, 45])
]

for child in t.children:
    child.parent = t

# 6장 10~14쪽 - 키 삽입 예제
for x in [9, 31, 5, 39, 23, 35, 36, 32]:
    t = BTreeInsert(t, x)

print("삽입 결과:")
printTree(t)