# 개잘했다 스고이
from collections import deque

n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

nx = [1,-1,0,0]
ny = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            newX = x + nx[i]
            newY = y + ny[i]

            if newX <0 or newY <0 or newX>=n or newY >=m:
                continue

            if graph[newX][newY]==1:
                continue

            if graph[newX][newY]==0:
                graph[newX][newY]=1
                queue.append((newX,newY))


count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            bfs(i,j)
            count+=1

print(count)
