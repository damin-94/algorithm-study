# 4장 11쪽 - 삽입 정렬
def insertionSort(A, n):
    for i in range(1, n):
        newitem = A[i]
        j = i - 1

        while j >= 0 and newitem < A[j]:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = newitem


# 추가 테스트
A = [5, 2, 4, 3]
print("정렬 전:", A)
insertionSort(A, len(A))
print("정렬 후:", A)