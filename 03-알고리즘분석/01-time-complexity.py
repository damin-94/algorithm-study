# 3장 12쪽 - 배열 가운데 인덱스의 값 반환
def function1(A, n):
    k = n // 2
    return A[k]


# 3장 13쪽 - 배열의 모든 원소 더하기
def function2(A, n):
    sum = 0
    for i in range(n):
        sum = sum + A[i]
    return sum


# 3장 14쪽 - 모든 A[i], A[j] 조합의 곱을 더하기
def function3(A, n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum = sum + A[i] * A[j]
    return sum


# 추가 테스트 
A = [1, 2, 3, 4, 5]
n = len(A)

print("function1:", function1(A, n))
print("function2:", function2(A, n))
print("function3:", function3(A, n))