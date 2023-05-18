import sys
from collections import deque
n, m, v = map(int,input().split())

graph = [[]for _ in range(n+1)]


for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


visited = [False]*(n+1)

def dfs(start):
    print(start,end=' ')
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(v)
print()
visited = [False]*(n+1)

def bfs(start):

    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(v)











