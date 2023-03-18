import sys
from collections import deque


n, m ,t = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(n+1):
    graph[i].sort()


def dfs(graph, v, visited):

    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        a = queue.popleft()
        print(a, end =' ')

        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(graph, t, visited)
visited = [False] * (n+1)
print('')
bfs(graph, t, visited)