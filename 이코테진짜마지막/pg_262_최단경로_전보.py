import heapq

n, m, start = map(int,input().split())

graph = [[] for _ in range(n+1)]

INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    
    graph[a].append((b,c))
    

def dij(start):
    
    q = []

    distance[start] =0
    
    heapq.heappush(q,(0,start))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
dij(start)

maxval = 0

count = 0

for i in distance:
    
    if i !=INF:
        count += 1
        maxval = max(maxval, i)
        
print(count-1, maxval)