# 3장 18쪽 - 재귀함수로 팩토리얼 계산
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


# 추가 테스트
print("factorial(1):", factorial(1))
print("factorial(5):", factorial(5))