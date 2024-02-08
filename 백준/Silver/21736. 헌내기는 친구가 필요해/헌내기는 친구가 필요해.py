import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
    graph.append(list(map(str,sys.stdin.readline())))

visited = [[False]*m for _ in range(n)]

def find(n, m):
    for i in range(n):
        for t in range(m):
            if graph[i][t] == 'I':
                return i,t

i, t = find(n,m)

direction = [(0,1),(0,-1),(1,0),(-1,0)]

count = 0

queue = deque([(i,t)])

visited[i][t] = True

while queue:
    x, y = queue.popleft()

    for nx,ny in direction:
        newX = x+nx
        newY = y+ny

        if 0<=newX <n and 0<=newY <m:

            if visited[newX][newY] ==False and graph[newX][newY]!='X':
                queue.append((newX,newY))
                visited[newX][newY] = True

                if graph[newX][newY]=='P':
                    count+=1


if count==0:
    print('TT')
else:
    print(count)
    