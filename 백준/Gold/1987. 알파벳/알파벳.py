import sys
from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

answer = 0
check = [0] * (26)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 1

def bfs(x, y):

    global answer
    q = set([(x,y,graph[x][y])])

    while q:
        x, y, alpha = q.pop()
        for i in range(4):
            newX = x+dx[i]
            newY = y+dy[i]

            if 0<=newX<n and 0<=newY<m and graph[newX][newY] not in alpha:
                q.add((newX,newY, alpha+graph[newX][newY]))
                answer = max(answer, len(alpha)+1)

bfs(0,0)
print(answer)

