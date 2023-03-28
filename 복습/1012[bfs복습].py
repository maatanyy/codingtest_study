import sys
from collections import deque

num = int(input())

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0

    while queue:
        a,b = queue.popleft()
        for i in range(4):
            newx = a+nx[i]
            newy = b+ny[i]

            if 0<=newx<m and 0<=newy<n and graph[newx][newy]==1:
                graph[newx][newy] = 0
                queue.append((newx, newy))




for _ in range(num):
    # 10,8, 17 8행 10열
    n, m, c = map(int,input().split())
    graph = [[0 for _ in range(n)] for _ in range(m)]

    for _ in range(c):
        a, b = map(int,sys.stdin.readline().split())
        graph[b][a] = 1


    count = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j]==1:
                bfs(i,j)
                count+=1

    print(count)

