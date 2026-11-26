# 2장 Part 2, 9쪽 - 중첩 리스트(Nested List)

nested_tree = [
    'A',
    ['B', ['C'], ['D', ['E'], ['F']]],
    ['G', ['H']],
    ['I', ['J', ['K']]]
]

# 2장 Part 2, 10쪽 - 인접 리스트(Adjacency List)
Tree = {
    'A': ['B', 'G', 'I'],
    'B': ['C', 'D'],
    'G': ['H'],
    'I': ['J'],
    'C': [],
    'D': ['E', 'F'],
    'H': [],
    'J': ['K'],
    'E': [],
    'F': [],
    'K': []
}

# 추가 테스트 
print("중첩 리스트에서 D 부분:", nested_tree[1][2])
print("인접 리스트에서 D의 자식:", Tree['D'])
print("인접 리스트에서 E의 자식:", Tree['E'])