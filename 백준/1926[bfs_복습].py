import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
# n은 세로 m은 가로

graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

nx = [-1,1,0,0]
ny = [0,0,-1,1]

ans = 0

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    count = 1

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            newx = a +nx[i]
            newy = b +ny[i]

            if 0<= newx <n and 0<=newy <m and graph[newx][newy]==1:
                queue.append((newx,newy))
                count+=1
                graph[newx][newy]=0

    return count

num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            num+=1
            val = bfs(i,j)
            ans = max(ans,val)


print(num)
print(ans)

