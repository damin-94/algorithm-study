# 7장 22쪽 - 개방 주소 방법(Open Addressing)

m = 13
NIL = None
DELETED = "DELETED"


# 7장 18쪽 - 선형 조사 해시 함수
def h(x):
    return x % m


def hi(x, i):
    return (h(x) + i) % m


# 7장 22쪽 - 해시 테이블 삽입
def hashInsert(T, x):
    i = 0

    while i < m:
        j = hi(x, i)

        # 빈자리 또는 삭제된 자리에 삽입
        if T[j] == NIL or T[j] == DELETED:
            T[j] = x
            return j

        else:
            i += 1

    print("테이블 오버플로우")
    return NIL


# 7장 22쪽 - 해시 테이블 검색
def hashSearch(T, x):
    i = 0

    while i < m:
        j = hi(x, i)

        # 검색 성공
        if T[j] == x:
            return j

        # 빈자리에 도달하면 검색 실패
        if T[j] == NIL:
            return NIL

        i += 1

    return NIL


# 7장 17쪽 - 실행 예제
T = [NIL] * m
A = [25, 13, 16, 15, 7, 28, 31, 20, 1, 38]

for x in A:
    hashInsert(T, x)

print("Hash Table:", T)

# 검색 연산 확인
print("28 검색:", hashSearch(T, 28))
print("38 검색:", hashSearch(T, 38))
print("100 검색:", hashSearch(T, 100))