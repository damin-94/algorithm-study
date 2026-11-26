# 4장 54쪽 - Python Sort

A = [4, 2, 8, 7, 3, 3, 5, 1, 9]

# sorted(): 정렬된 새로운 리스트 반환
B = sorted(A)

print("원본:", A)
print("sorted():", B)

# sort(): 기존 리스트를 직접 정렬
A.sort()

print("sort():", A)