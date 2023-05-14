import sys
import heapq
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] * (n+1) for _ in range(n+1)]

for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())

    graph[a].append((b,c))
    graph[b].append((a,c))

u, v = map(int,input().split())

def dijstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance


x = dijstra(1)
y = dijstra(u)
z = dijstra(v)

ans1 = x[u] + y[v] + z[n]
ans2 = x[v] + z[u] + y[n]

answer = min(ans1,ans2)

if answer>=INF:
    print(-1)
else:
    print(answer)