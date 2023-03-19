import sys
from collections import deque

n, m = map(int,input().split())
# n 세로, m 가로

graph = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(input()))

count = 0
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        if graph[x][y] == '-':
            if y+1 <m and graph[x][y+1] == '-' and visited[x][y+1] == False:
                visited[x][y+1]=True
                queue.append((x,y+1))

        elif graph[x][y] == '|':
            if x+1 < n and graph[x+1][y] =='|' and visited[x+1][y] == False:
                visited[x+1][y] = True
                queue.append((x+1,y))

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            bfs(i,j)
            count = count+1

print(count)



