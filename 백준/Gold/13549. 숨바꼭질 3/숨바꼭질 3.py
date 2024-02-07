import sys
import heapq

INF = int(1e9)

n, m = map(int,input().split())

distance = [INF] * 100001


def dij(start):

    distance[start] = 0
    q = []

    heapq.heappush(q,(0,start))

    while q:

        time, now = heapq.heappop(q)

        if distance[now] < time:
            continue

        for i in range(3):

            if i==0 and 2*now <= 100000:
                
                if time < distance[2*now]:
                    distance[2*now] = time
                    heapq.heappush(q,(time,2*now))
            
            elif i==1 and now+1 <=100000:

                if time+1 < distance[now+1]:
                    distance[now+1] = time+1
                    heapq.heappush(q,(time+1,now+1))

            elif i==2 and now-1 >= 0:

                if time+1 < distance[now-1]:
                    distance[now-1] = time+1
                    heapq.heappush(q,(time+1,now-1))
            


dij(n)
print(distance[m])