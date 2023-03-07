import heapq
import sys

num = int(input())

h = []
result = []

for _ in range(num):
    value = int(sys.stdin.readline())
    heapq.heappush(h, value)

for _ in range(len(h)):
    result.append(heapq.heappop(h))

for i in result:
    print(i)