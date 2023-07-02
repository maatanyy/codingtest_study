import heapq
import sys
num = int(input())

values = []

for _ in range(num):
    values.append(list(map(int, sys.stdin.readline().split())))

values.sort()

ans = []

heapq.heappush(ans, values[0][1])

for i in range(1, num):
    if values[i][0] < ans[0]:
        heapq.heappush(ans,values[i][1])

    else:
        heapq.heappop(ans)
        heapq.heappush(ans,values[i][1])

print(len(ans))

