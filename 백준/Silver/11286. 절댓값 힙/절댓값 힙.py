import heapq
import sys

num = int(sys.stdin.readline())

q =  []

for _ in range(num):

    temp = int(sys.stdin.readline())

    if temp != 0:
        heapq.heappush(q,[abs(temp),temp])

    if temp == 0:
        
        if len(q) ==0:
            print('0')
        
        else:
            a = heapq.heappop(q)
            print(a[1])