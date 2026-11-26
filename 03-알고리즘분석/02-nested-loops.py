# 3장 15쪽 - 매번 배열의 최댓값을 찾아 더하기
def function4(A, n):
    sum = 0
    for i in range(n):
        for j in range(n):
            k = max(A)
            sum = sum + k
    return sum


# 3장 16~17쪽 - i보다 뒤에 있는 원소와만 짝지어 곱하기
def function5(A, n):
    sum = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum = sum + A[i] * A[j]
    return sum


# 추가 테스트
A = [1, 2, 3, 4, 5]
n = len(A)

print("function4:", function4(A, n))
print("function5:", function5(A, n))