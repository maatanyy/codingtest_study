INF = int(1e9)

n, m = map(int,input().split())

graph = [ [INF]* (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0


for _ in range(m):
    x, y = map(int,input().split())
    graph[x][y] = 1
    graph[y][x] = 1

st, en = map(int,input().split())

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

distance = graph[1][en]+graph[en][st]

if distance>=INF:
    print("-1")
else:
    print(distance)

