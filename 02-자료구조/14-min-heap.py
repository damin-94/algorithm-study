# 2장 Part 2, 40쪽 - heapq로 최소 힙 실습
import heapq

h = list()

heapq.heappush(h, 10)
heapq.heappush(h, 43)
heapq.heappush(h, 76)
heapq.heappush(h, 5)

print("삽입 후:", h)
print("꺼낸 값:", heapq.heappop(h))
print("삭제 후:", h)