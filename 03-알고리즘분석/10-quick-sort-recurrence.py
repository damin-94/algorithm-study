# 3장 57~60쪽 - 퀵 정렬의 분할 크기와 점화식
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # 추가 테스트 - 재귀 호출 직전의 분할 크기 확인
    print(f"n={len(arr)}, pivot={pivot}, 왼쪽={len(left)}, 오른쪽={len(right)}")

    return quick_sort(left) + middle + quick_sort(right)


print("[균형 있게 나뉘는 경우]")
print(quick_sort([1, 2, 3, 4, 5]))

print("[한쪽으로만 나뉘는 경우]")
print(quick_sort([4, 2, 1, 3, 5]))