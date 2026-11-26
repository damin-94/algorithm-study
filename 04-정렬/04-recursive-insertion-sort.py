# 4장 14쪽 - 재귀 삽입 정렬
def insertionSort(A, n):
    if n > 1:
        # 앞의 n-1개를 먼저 정렬한다.
        insertionSort(A, n - 1)

        # 마지막 값을 정렬된 구간의 알맞은 자리에 넣는다.
        newitem = A[n - 1]
        j = n - 2

        while j >= 0 and newitem < A[j]:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = newitem


# 테스트 코드
A = [5, 2, 4, 3]
n = 4

print("정렬 전:", A)
insertionSort(A, n)
print("정렬 후:", A)