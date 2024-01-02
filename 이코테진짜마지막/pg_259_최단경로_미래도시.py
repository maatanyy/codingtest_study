n, m = map(int, input().split())

graph = [[100]*(n+1) for _ in range(n+1)]


for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0
            

for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    

start, end = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            

distance = graph[1][end] + graph[end][start]

if distance >=100:
    print('-1')
else:
    print(distance)
    
    
    