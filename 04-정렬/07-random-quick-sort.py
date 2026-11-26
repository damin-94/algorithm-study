import random


def quickSort(A, p, r):
    if p < r:
        k = random.randint(p, r)      # 26쪽 - 피벗 위치를 무작위로 선택
        A[k], A[r] = A[r], A[k]      # 26쪽 - 선택한 값을 맨 끝으로 이동

        q = partition2(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def partition2(A, p, r):
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

print("정렬 전:", A)
quickSort(A, 0, len(A) - 1)
print("정렬 후:", A)