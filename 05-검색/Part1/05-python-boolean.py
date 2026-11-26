# 5장 Part1 22쪽 - AND OR IN PYTHON

# False로 판단되는 값
for value in ('', 0, None, [], (), {}, False):
    if value:
        print(value, "True")
    else:
        print(value, "False")

# True로 판단되는 값
for value in (' ', 2, 1, "a", [1], (3,), True):
    if value:
        print(value, "True")
    else:
        print(value, "False")