# 7장 17~18쪽 - 선형 조사(Linear Probing)

# 해시 테이블 생성
m = 13
HashTable = [None] * m


# 기본 해시 함수
def h(x):
    return x % m


# 7장 18쪽 - 선형 조사 해시 함수
def hi(x, i):
    return (h(x) + i) % m


# 선형 조사를 이용한 삽입
def insert(x):
    for i in range(m):
        index = hi(x, i)

        # 빈자리를 찾으면 삽입
        if HashTable[index] is None:
            HashTable[index] = x
            return

    print("Hash Table is full")


# 해시 테이블 출력
def printTable():
    for i in range(m):
        print(i, ":", HashTable[i])


# 7장 17쪽 - 실행 예제
A = [25, 13, 16, 15, 7, 28, 31, 20, 1, 38]

for x in A:
    insert(x)

printTable()