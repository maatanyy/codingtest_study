from collections import deque

n, m = map(int,input().split())

graph = [list(input()) for _ in range(m)]

visited = [[False for _ in range(n)] for _ in range(m)]

nx = [1,-1,0,0]
ny = [0,0,1,-1]

width1 = 0
width2 = 0

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y]=True
    count=1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            ax = x + nx[i]
            ay = y + ny[i]

            if 0<= ax< m and 0<=ay <n and graph[x][y]==graph[ax][ay] and visited[ax][ay]==False:
                count+=1
                queue.append((ax,ay))
                visited[ax][ay] = True

    return count

for i in range(m):
    for j in range(n):
        if visited[i][j]==False:
            ans = bfs(i,j)

            if graph[i][j]=='W':
                width1 += ans **2

            else:
                width2 += ans **2

print(width1,width2)
