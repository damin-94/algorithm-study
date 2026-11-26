# 4장 22쪽 - 퀵 정렬
def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


# 4장 23쪽 - 마지막 원소를 피벗으로 분할
def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# 추가 테스트 
A = [31, 8, 48, 73, 11, 3, 20, 29, 65, 15]

# 복사본으로 첫 분할만 확인
B = A[:]
q = partition(B, 0, len(B) - 1)
print("첫 분할 후:", B)
print("피벗 위치:", q)

# 원래 배열로 전체 정렬
quickSort(A, 0, len(A) - 1)
print("정렬 후:", A)