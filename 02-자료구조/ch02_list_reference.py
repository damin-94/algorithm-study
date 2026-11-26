# 2장 17쪽 - 리스트 객체 참조
x = [1, 2, [100, 200], [1000, 2000, 3000], 4, 5]

y = x[2]
print("추가 전 y =", y)

y.append(500)
print("추가 후 y =", y)
print("추가 후 x =", x)

# 2장 18쪽 - 리스트 복사( b = a )
print("\n[1] b = a")
a = [1, 2, 3]
b = a
b.append(5)
print("a =", a)
print("b =", b)

# 2장 18쪽 - 리스트 복사( b = a[:] )
print("\n[2] b = a[:]")
a = [1, 2, 3]
b = a[:]
b.append(5)
print("a =", a)
print("b =", b)

# 2장 18쪽 - 리스트 복사( 바깥 리스트에 5 추가 )
print("\n[3] 바깥 리스트에 추가")
a = [[1, 2], [3, 4]]
b = a[:]
b.append(5)
print("a =", a)
print("b =", b)

# 2장 18쪽 - 리스트 복사( 안쪽 리스트에 5 추가 )
print("\n[4] 안쪽 리스트에 추가")
a = [[1, 2], [3, 4]]
b = a[:]
a[1].append(5)
print("a =", a)
print("b =", b)
