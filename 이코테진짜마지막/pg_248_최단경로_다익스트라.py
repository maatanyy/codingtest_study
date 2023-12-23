import heapq
import sys

n, m  = map(int,input().split())

start = int(input())

graph = [[] for _ in range(n+1)]

distance = [1e9] * (n+1)


for _ in range(m):
    
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    
def dij(start):
    
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        
        dist, now  = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            
            cost = dist+i[1]
            
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dij(start)
                

for i in range(1, n+1):
    
    if distance[i] == 1e9:
        print('INFINITY')
    
    else:
        print(distance[i])