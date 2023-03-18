import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

nx = [-1,1,0,0]
ny = [0,0,1,-1]

total = 0
graph = []
ans = 0
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    ground = 1

    while queue:
        ax, ay = queue.popleft()

        for i in range(4):
            nexX = ax +nx[i]
            newY = ay +ny[i]

            if nexX<0 or nexX>= n or newY<0 or newY>=m:
                continue

            if graph[nexX][newY]==1:
                graph[nexX][newY] = 0
                queue.append((nexX, newY))
                ground += 1

    return ground

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            ans = max(ans,bfs(i,j))
            total+=1

print(total)
print(ans)

