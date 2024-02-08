import sys
from collections import deque
num = int(input())

graph = [[-1]* (num) for _ in range(num)]
visited = [[False]*(num) for _ in range(num)]

r1, c1, r2, c2 = map(int,input().split())

# r1,c1 에서 r2,c2로

queue = deque([[r1,c1]])

ways = [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]

graph[r1][c1] = 0
visited[r1][c1] = True

while queue:

    x,y = queue.popleft()

    for i in ways:

        newX = x+i[0]
        newY = y+i[1]

        if 0<=newX < num and 0<=newY <num and visited[newX][newY] == False:
            graph[newX][newY] = graph[x][y]+1
            visited[newX][newY] = True
            queue.append([newX,newY])


if graph[r2][c2] == -1:
    print('-1')
else:
    print(graph[r2][c2])