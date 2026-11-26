# 7장 25쪽 - 재해싱(Rehashing)

m = 13
NIL = None

def h(x, m):
    return x % m


def hi(x, i, m):
    return (h(x, m) + i) % m


def hashInsert(T, x):
    m = len(T)

    for i in range(m):
        j = hi(x, i, m)

        if T[j] == NIL:
            T[j] = x
            return j

    return NIL


# 7장 25쪽 - 재해싱
def rehashing(T):
    # 새로운 해시 테이블 생성
    new_m = 29
    new_T = [NIL] * new_m

    # 기존 원소를 새로운 테이블에 다시 삽입
    for x in T:
        if x != NIL:
            hashInsert(new_T, x)

    return new_T


# 실행 예제
T = [NIL] * m
A = [25, 13, 16, 15, 7, 28, 31, 20, 1, 38]

for x in A:
    hashInsert(T, x)

# 해시 테이블 공간 사용률 계산
count = sum(x != NIL for x in T)
loadFactor = count / len(T)

print("재해싱 전 크기:", len(T))
print("공간 사용률:", round(loadFactor * 100, 2), "%")

# 공간 사용률이 75% 이상이면 재해싱
if loadFactor >= 0.75:
    T = rehashing(T)

print("재해싱 후 크기:", len(T))
print("공간 사용률:", round(count / len(T) * 100, 2), "%")