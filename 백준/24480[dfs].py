import sys
sys.setrecursionlimit(200000)

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(v):
    global count
    count += 1
    visited[v] = count
    for n in sorted(graph[v], reverse=True):
        if not visited[n]:
            dfs(n)

dfs(r)

print('\n'.join(map(str, visited[1:])))
