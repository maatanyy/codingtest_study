import heapq
INF = int(1e9)

n,m,start = map(int,input().split())

graph = [[]for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dij(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dis, nod = heapq.heappop(q)

        if distance[nod] < dis:
            continue

        for i in graph[nod]:
            cost = dis + i[1]

            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dij(start)

count = 0

max_dis = 0

for i in distance:
    if i!=INF:
        count+=1
        max_dis = max(max_dis,i)

print(count-1, max_dis)