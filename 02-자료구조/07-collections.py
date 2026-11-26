# 60쪽 왼쪽 - Counter
from collections import Counter

data = ['A', 'B', 'A', 'C', 'A', 'B']

count = Counter(data)
print(count)

# 60쪽 오른쪽 - defaultdict
from collections import defaultdict

graph = defaultdict(list)

graph['A'].append('B')
graph['A'].append('C')

print(graph['A'])