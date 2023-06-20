import heapq

INF = int(1e9)

x, y, start = map(int,input().split())

graph = [[]for i in range(x+1)]
distance = [INF] * (x+1)

for i in range(y):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dij(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] <dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dij(start)
mx = -1

count = 0
for i in range(1, x+1):
    if distance[i]!=INF:
        count+=1
        mx = max(mx,distance[i])

print(count-1, mx)















