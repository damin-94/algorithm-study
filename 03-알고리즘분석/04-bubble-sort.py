# 3장 27쪽 - 버블 정렬
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# 추가 테스트
arr = [5, 1, 4, 2, 3]
print("정렬 전:", arr)
print("정렬 후:", bubble_sort(arr))