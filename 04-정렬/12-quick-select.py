# 4장 23쪽 - 분할(Partition)
def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


# 4장 57쪽 - Quick Select
def select(A, p, r, i):
    # 원소가 하나인 경우
    if p == r:
        return A[p]

    q = partition(A, p, r)
    k = q - p + 1

    # 왼쪽 그룹에서 탐색
    if i < k:
        return select(A, p, q - 1, i)

    # 기준 원소가 찾는 원소인 경우
    elif i == k:
        return A[q]

    # 오른쪽 그룹에서 탐색
    else:
        return select(A, q + 1, r, i - k)


# 테스트 코드
A = [31, 8, 48, 73, 11, 3, 20, 29, 65, 15]

print("원본:", A)
print("2번째 작은 원소:", select(A, 0, len(A) - 1, 2))
print("7번째 작은 원소:", select(A, 0, len(A) - 1, 7))