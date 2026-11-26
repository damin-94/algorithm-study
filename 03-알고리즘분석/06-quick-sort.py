# 3장 30쪽 - 재귀 퀵 정렬
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# 테스트 코드
arr = [9, 8, 6, 12, 5, 7, 4, 10, 1, 14, 17, 20, 3, 11, 15]
print("정렬 전:", arr)
print("정렬 후:", quick_sort(arr))