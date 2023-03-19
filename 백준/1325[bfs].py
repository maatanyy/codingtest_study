import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
# n 컴퓨터 수 m 엣지수

graph = [[] * (n+1) for i in range(n+1)]
ans = []

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[b].append(a)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [False] * (n+1)
    visited[start] = True
    count = 1

    while queue:
        ne = queue.popleft()

        for i in graph[ne]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count+=1


    return count

top = -1
for i in range(1,n+1):
    temp = bfs(i)

    if temp >top:
        top = temp
        ans.clear()
        ans.append(i)

    elif temp==top:
        ans.append(i)

for i in ans:
    print(i, end =' ')