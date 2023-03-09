import heapq
import sys


INF =int(1e9)

n, m = map(int,input().split())
# n은 노드의 개수
start = int(input())

graph = [ [] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
        ## b 노르도 가는 c비용
def dij(start):
    q = []

    heapq.heappush(q,(0, start))
    distance[start]=0

    while q:
        dis, nod = heapq.heappop(q)

        if distance[nod] < dis:
            continue

        for i in graph[nod]:
            cost = dis+i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dij(start)

for i in range(1,n+1):

    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])