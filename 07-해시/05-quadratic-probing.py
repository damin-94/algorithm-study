# 7장 19~20쪽 - 이차원 조사(Quadratic Probing)

# 해시 테이블 생성
m = 13
HashTable = [None] * m


# 기본 해시 함수
def h(x):
    return x % m


# 7장 20쪽 - 이차원 조사 해시 함수
def hi(x, i):
    return (h(x) + i ** 2) % m


# 이차원 조사를 이용한 삽입
def insert(x):
    for i in range(m):
        index = hi(x, i)

        # 빈자리를 찾으면 삽입
        if HashTable[index] is None:
            HashTable[index] = x
            return

    print("삽입할 위치를 찾지 못함")


# 해시 테이블 출력
def printTable():
    for i in range(m):
        print(i, ":", HashTable[i])


# 7장 19쪽 - 실행 예제
A = [15, 28, 41, 67, 54]

for x in A:
    insert(x)

printTable()