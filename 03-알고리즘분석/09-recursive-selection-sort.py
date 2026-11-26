# 3장 55쪽 - 재귀 선택 정렬
def recursive_selection_sort(arr, n):
    if n <= 1:
        return

    # 앞의 n개 원소 중 가장 큰 값의 인덱스 찾기
    max_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i

    # 최댓값을 현재 구간의 맨 뒤로 보내기
    arr[n - 1], arr[max_idx] = arr[max_idx], arr[n - 1]

    recursive_selection_sort(arr, n - 1)


# 추가 테스트
arr = [5, 1, 4, 2, 3]
print("정렬 전:", arr)
recursive_selection_sort(arr, len(arr))
print("정렬 후:", arr)