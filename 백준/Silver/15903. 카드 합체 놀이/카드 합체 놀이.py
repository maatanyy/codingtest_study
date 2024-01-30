import sys
import heapq

n, m = map(int,sys.stdin.readline().split())

q = []

temp = list(map(int,sys.stdin.readline().split()))

for i in temp:
    heapq.heappush(q,i)


for _ in range(m):

    a = heapq.heappop(q)
    b = heapq.heappop(q)

    heapq.heappush(q,a+b)
    heapq.heappush(q,a+b)

print(sum(q))