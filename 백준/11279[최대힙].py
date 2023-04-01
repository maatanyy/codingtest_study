import sys
import heapq

num = int(sys.stdin.readline())
q = []
for _ in range(num):
    temp = int(sys.stdin.readline())
    if temp==0:
        if len(q)==0:
            print(0)
        else:
            x = heapq.heappop(q)
            print(-x)
    else:
        heapq.heappush(q,-temp)