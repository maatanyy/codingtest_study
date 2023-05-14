import heapq
import sys
n, m = map(int, sys.stdin.readline().split())

start = int(input())

INF = int(1e9)

graph = [ []*(n+1) for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

def dij(start):

    q = []
    heapq.heappush(q,(0, start))  #거리, 노드
    distance[start] = 0

    while q:
        dis, nod = heapq.heappop(q)

        if distance[nod] < dis:
            continue

        for i in graph[nod]:
            cost = dis + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dij(start)

for i in range(len(distance)-1):
    if distance[i+1]== INF:
        print('INF')
    else:
        print(distance[i+1])







