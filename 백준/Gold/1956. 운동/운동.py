import sys

INF = int(1e9)
small = INF * 2
n, m = map(int, sys.stdin.readline().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    if graph[a][a] <= small:
        small = graph[a][a]

if small == INF:
    print('-1')
else:
    print(small)