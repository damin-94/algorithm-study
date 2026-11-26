# 4장 29쪽 - 스며내리기
def percolateDown(A, k):
    n = len(A)
    child = 2 * k + 1  # 왼쪽 자식
    right = 2 * k + 2  # 오른쪽 자식

    if child <= n - 1:
        # 두 자식 중 더 큰 값의 위치를 child에 저장
        if right <= n - 1 and A[child] < A[right]:
            child = right

        # 부모가 더 작으면 교환하고, 내려간 자리에서 다시 확인
        if A[k] < A[child]:
            A[k], A[child] = A[child], A[k]
            percolateDown(A, child)


# 4장 29쪽 - 최대 힙 구성
def buildHeap(A):
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):
        percolateDown(A, i)


# 테스트 코드
A = [4, 2, 8, 7, 3, 3, 5, 1, 9]

print("힙 구성 전:", A)
buildHeap(A)
print("힙 구성 후:", A)
print("루트:", A[0])