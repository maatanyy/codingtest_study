import sys
import heapq
import copy

INF = int(1e9)

n, m, x = map(int,sys.stdin.readline().split())

origin_distance = [INF] * (n+1)
distance2 = [INF] * (n+1)

graph = [[] *(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())

    graph[a].append((b,c))


def dij1(start):

    q = []
    heapq.heappush(q,(0, start))

    distance1[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if distance1[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance1[i[0]]:

                distance1[i[0]] = cost

                heapq.heappush(q,(cost,i[0]))


def dij2(start):

    q = []
    heapq.heappush(q,(0, start))

    distance2[start] = 0

    while q:

        dist, now = heapq.heappop(q)

        if distance2[now] < dist:
            continue

        for i in graph[now]:

            cost = dist + i[1]

            if cost < distance2[i[0]]:

                distance2[i[0]] = cost

                heapq.heappush(q,(cost,i[0]))

ans = -1

dij2(x)

for i in range(1,n+1):
    distance1 = copy.deepcopy(origin_distance)
    dij1(i)
    temp = 0
    temp += distance1[x]
    temp += distance2[i]

    ans = max(ans,temp)

print(ans)
