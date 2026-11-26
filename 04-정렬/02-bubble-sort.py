# 4장 8쪽 - 기본 버블 정렬
def bubbleSort(A, n):
    for last in range(n - 1, 0, -1):
        for i in range(last):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]


# 4장 10쪽 - 교환이 없으면 종료하는 버블 정렬
def bubbleSort2(A, n):
    sorted = False

    for last in range(n - 1, 0, -1):
        sorted = True

        for i in range(last):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                sorted = False

        if sorted:
            return


# 추가 테스트 
A = [5, 1, 4, 2, 3]
B = A[:]

bubbleSort(A, len(A))
bubbleSort2(B, len(B))

print("bubbleSort:", A)
print("bubbleSort2:", B)