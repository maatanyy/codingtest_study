import sys
from collections import deque

n,m,k = map(int,sys.stdin.readline().split())

graph = [[0 for _ in range(m+1)] for _ in range(n+1)]

nx = [1,-1,0,0]
ny = [0,0,1,-1]

for _ in range(k):
    a, b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    count = 1
    graph[x][y] = 0

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            newx = a+nx[i]
            newy = b+ny[i]

            if 0<=newx<n+1 and 0<=newy<m+1 and graph[newx][newy]==1:
                queue.append((newx,newy))
                graph[newx][newy]=0
                count+=1

    return count

val = -1
for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] == 1:
            val = max(val, bfs(i,j))

print(val)











