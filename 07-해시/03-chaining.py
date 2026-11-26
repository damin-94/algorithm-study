# 7장 13~14쪽 - 체이닝(Chaining)

# 연결 리스트 노드 정의
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


# 해시 테이블 생성
m = 13
HashTable = [None] * m


# 해시 함수
def h(x):
    return x % m


# 체이닝을 이용한 삽입
def insert(x):
    index = h(x)
    new_node = Node(x)

    # 해당 주소가 비어 있는 경우
    if HashTable[index] is None:
        HashTable[index] = new_node

    # 충돌 발생 시 연결 리스트에 추가
    else:
        p = HashTable[index]

        while p.next is not None:
            p = p.next

        p.next = new_node


# 해시 테이블 출력
def printTable():
    for i in range(m):
        print(i, ":", end=" ")

        p = HashTable[i]

        while p is not None:
            print(p.key, end=" -> ")
            p = p.next

        print("None")


# 7장 14쪽 - 실행 예제
A = [39, 13, 40, 94, 3, 42, 55,
     43, 44, 70, 86, 47, 74, 76]

for x in A:
    insert(x)

printTable()