import heapq
import sys

INF = int(1e9)
num = int(input())
edge = int(input())

graph = [[]*(num+1) for _ in range(num+1)]

for _ in range(edge):

    a, b, c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))


distance = [INF] * (num+1)

def dij(start):

    distance[start] = 0

    q =[]

    heapq.heappush(q,(0, start))

    while q:

        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))


start, goal = map(int,input().split())

dij(start)
print(distance[goal])



            

