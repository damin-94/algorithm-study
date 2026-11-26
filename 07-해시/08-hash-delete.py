# 7장 24쪽 - 해시 테이블 삭제

m = 13
NIL = None
DELETED = "DELETED"

def h(x):
    return x % m


def hi(x, i):
    return (h(x) + i) % m


def hashInsert(T, x):
    i = 0

    while i < m:
        j = hi(x, i)

        if T[j] == NIL or T[j] == DELETED:
            T[j] = x
            return j

        i += 1

    return NIL

def hashSearch(T, x):
    i = 0

    while i < m:
        j = hi(x, i)

        if T[j] == x:
            return j

        if T[j] == NIL:
            return NIL

        i += 1

    return NIL


# 7장 24쪽 - 삭제
def hashDelete(T, x):
    j = hashSearch(T, x)

    # 삭제된 위치에 DELETED 표시
    if j is not NIL:
        T[j] = DELETED
        return j

    return NIL


# 7장 24쪽 - 실행 예제
T = [NIL] * m
A = [25, 13, 16, 15, 7, 28, 31, 20, 1, 38]

for x in A:
    hashInsert(T, x)

print("삭제 전:", T)

# 1 삭제
hashDelete(T, 1)
print("삭제 후:", T)

# 삭제 이후에도 38을 검색할 수 있는지 확인
print("1 검색:", hashSearch(T, 1))
print("38 검색:", hashSearch(T, 38))