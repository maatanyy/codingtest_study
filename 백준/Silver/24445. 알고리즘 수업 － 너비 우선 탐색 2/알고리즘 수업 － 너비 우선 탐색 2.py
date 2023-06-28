from collections import deque
import sys
n, m, start = map(int, sys.stdin.readline().split())

graph = [[]for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort(reverse=True)

visited = [0] * (n+1)

count = 1

def bfs(start):
    global count

    q = deque([start])
    visited[start] = 1

    while q:
        v = q.popleft()
        for g in graph[v]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                q.append(g)
bfs(start)

for v in visited[1:]:
    print(v)








