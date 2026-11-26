K = 5

class Node:
    def __init__(self, keys=None):
        self.keys = keys if keys is not None else []
        self.children = []
        self.parent = None


# 삭제할 키를 가진 노드 검색
def BTreeSearch(t, x):
    i = 0

    while i < len(t.keys) and x > t.keys[i]:
        i += 1

    if i < len(t.keys) and x == t.keys[i]:
        return t

    if not t.children:
        return None

    return BTreeSearch(t.children[i], x)


# 6장 20쪽 - B-Tree 삭제
def BTreeDelete(t, x, v):
    if v is None:
        return t

    i = v.keys.index(x)

    # 리프 노드가 아닌 경우
    if v.children:
        r = v.children[i + 1]

        # 직후 원소를 가진 리프 노드 탐색
        while r.children:
            r = r.children[0]

        y = r.keys[0]

        # x와 y 교환
        v.keys[i] = y
        r.keys[0] = x

    else:
        r = v

    # 리프 노드에서 x 제거
    r.keys.remove(x)

    # 언더플로우 발생
    if len(r.keys) < K // 2:
        return clearUnderflow(r)

    return t


# 6장 20쪽 - 언더플로우 해결
def clearUnderflow(r):
    p = r.parent

    # 루트 노드 처리
    if p is None:
        if not r.keys and r.children:
            t = r.children[0]
            t.parent = None
            return t

        return r

    i = p.children.index(r)

    # 왼쪽 형제에게 키를 빌리는 경우
    if i > 0:
        left = p.children[i - 1]

        if len(left.keys) > K // 2:
            r.keys.insert(0, p.keys[i - 1])
            p.keys[i - 1] = left.keys.pop()

            if left.children:
                child = left.children.pop()
                r.children.insert(0, child)
                child.parent = r

            return getRoot(p)

    # 오른쪽 형제에게 키를 빌리는 경우
    if i < len(p.children) - 1:
        right = p.children[i + 1]

        if len(right.keys) > K // 2:
            r.keys.append(p.keys[i])
            p.keys[i] = right.keys.pop(0)

            if right.children:
                child = right.children.pop(0)
                r.children.append(child)
                child.parent = r

            return getRoot(p)

    # 왼쪽 형제와 병합
    if i > 0:
        left = p.children[i - 1]

        left.keys.append(p.keys.pop(i - 1))
        left.keys.extend(r.keys)

        for child in r.children:
            left.children.append(child)
            child.parent = left

        p.children.pop(i)

    # 오른쪽 형제와 병합
    else:
        right = p.children[i + 1]

        r.keys.append(p.keys.pop(i))
        r.keys.extend(right.keys)

        for child in right.children:
            r.children.append(child)
            child.parent = r

        p.children.pop(i + 1)

    # 부모 노드의 언더플로우 확인
    if len(p.keys) < K // 2:
        return clearUnderflow(p)

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


# 6장 17쪽 - 초기 B-Tree 구성
t = Node([15])

t.children = [
    Node([4, 8]),
    Node([19, 22])
]

t.children[0].children = [
    Node([1, 2, 3]),
    Node([5, 6, 7]),
    Node([9, 10])
]

t.children[1].children = [
    Node([16, 18]),
    Node([20, 21]),
    Node([24, 25, 26])
]

for child in t.children:
    child.parent = t

    for leaf in child.children:
        leaf.parent = child


# 6장 17~19쪽 - 삭제 실행 예제
print("삭제 전:")
printTree(t)

for x in [7, 4, 9]:
    v = BTreeSearch(t, x)
    t = BTreeDelete(t, x, v)

    print("\n", x, "삭제 후:")
    printTree(t)