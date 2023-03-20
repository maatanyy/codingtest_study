import sys
from collections import deque

m, n= map(int,sys.stdin.readline().split())
#m 세로 n 가로

graph = []

nx = [1,-1,0,0,1,1,-1,-1]
ny = [0,0,1,-1,1,-1,-1,1]

for _ in range(m):
    graph.append(list(map(int,sys.stdin.readline().split())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            dx = x+nx[i]
            dy = y+ny[i]
            if 0<=dx<m and 0<=dy<n and graph[dx][dy]==1:
                queue.append((dx,dy))
                graph[dx][dy]=0


count = 0

for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j)
            count+=1

print(count)


