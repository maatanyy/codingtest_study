import sys
import heapq

x = int(input())
arr=[]

for _ in range(x):
    heapq.heappush(arr, int(sys.stdin.readline()))

if len(arr) == 1:
    print(0)

else:
    answer = 0
    while len(arr) > 1:
        tempval1 = heapq.heappop(arr)
        tempval2 = heapq.heappop(arr)
        answer += tempval1 + tempval2
        heapq.heappush(arr, tempval1 + tempval2)

    print(answer)