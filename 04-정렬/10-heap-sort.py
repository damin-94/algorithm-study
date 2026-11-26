# 4장 29쪽 - 스며내리기
def percolateDown(A, k, n):
    child = 2 * k + 1
    right = 2 * k + 2

    if child <= n - 1:
        # 두 자식 중 더 큰 원소 선택
        if right <= n - 1 and A[child] < A[right]:
            child = right

        # 부모와 자식 비교 및 교환
        if A[k] < A[child]:
            A[k], A[child] = A[child], A[k]
            percolateDown(A, child, n)


# 4장 29쪽 - 최대 힙 구성
def buildHeap(A):
    n = len(A)

    for i in range((n - 2) // 2, -1, -1):
        percolateDown(A, i, n)


# 4장 45쪽 - 최대 원소 삭제
def deleteMax(A, n):
    max = A[0]
    A[0] = A[n - 1]
    n -= 1

    percolateDown(A, 0, n)
    return max


# 4장 50쪽 - 힙 정렬
def heapSort(A):
    n = len(A)
    buildHeap(A)

    # 최대 원소를 배열 뒤쪽부터 저장
    for i in range(n - 1, 0, -1):
        A[i] = deleteMax(A, i + 1)


# 테스트 코드
A = [4, 2, 8, 7, 3, 3, 5, 1, 9]

print("정렬 전:", A)
heapSort(A)
print("정렬 후:", A)