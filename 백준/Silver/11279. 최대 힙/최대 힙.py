import heapq
import sys

num = int(sys.stdin.readline())

q = []

for _ in range(num):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(q)==0:
            print(0)
        else:
            val = heapq.heappop(q)
            print(-val)


    else:
        heapq.heappush(q,-x)
