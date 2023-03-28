import sys
from collections import deque

n,m = map(int, input().split())

graph = [list(map(int,input())) for _ in range(n)]

nx = [1,-1,0,0]
ny = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        a,b = queue.popleft()

        for i in range(4):
            newx = a+nx[i]
            newy = b+ny[i]

            if 0<=newx<n and 0<=newy<m and graph[newx][newy]==1:
                graph[newx][newy] = graph[a][b]+1
                queue.append((newx,newy))

    return graph[n-1][m-1]

print(bfs(0,0))
