# 4장 15쪽 - 병합 정렬
def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    i = p       
    j = q + 1   
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    tmp.extend(A[i:q + 1])
    tmp.extend(A[j:r + 1])

    A[p:r + 1] = tmp


# 추가 테스트
A = [5, 2, 4, 3]
print("정렬 전:", A)
mergeSort(A, 0, len(A) - 1)
print("정렬 후:", A)