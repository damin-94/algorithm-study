# 3장 52쪽 - 재귀 호출로 리스트의 합 구하기
def RecurrenceSum(arr):
    if len(arr) == 1:
        return arr[0]

    return RecurrenceSum(arr[1:]) + arr[0]


# 추가 테스트 
print("원소 1개:", RecurrenceSum([5]))
print("원소 4개:", RecurrenceSum([1, 2, 3, 4]))