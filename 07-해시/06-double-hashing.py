# 7장 21쪽 - 더블 해싱(Double Hashing)

# 해시 테이블 생성
m = 13
HashTable = [None] * m


# 기본 해시 함수
def h(x):
    return x % 13


# 두 번째 해시 함수
def f(x):
    return 1 + (x % 11)


# 7장 21쪽 - 더블 해싱 함수
def hi(x, i):
    return (h(x) + i * f(x)) % m


# 더블 해싱을 이용한 삽입
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


# 7장 21쪽 - 실행 예제
A = [15, 19, 28, 41, 67]

for x in A:
    insert(x)

printTable()