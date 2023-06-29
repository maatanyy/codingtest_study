import sys
from collections import deque

m,n,k = map(int,input().split())

graph = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(k):
    a,b,c,d = map(int,input().split())
    # 0~4, 2~4
    for i in range(b,d):  #2,4
        for j in range(a,c):  #0,4
            graph[i][j] = 1


nx = [1,-1,0,0]
ny = [0,0,1,-1]

def bfs(x,y):
    count = 1
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1

    while queue:
        a,b = queue.popleft()

        for i in range(4):
            newx = a+nx[i]
            newy = b+ny[i]

            if 0<=newx<m and 0<=newy<n and graph[newx][newy]==0:
                graph[newx][newy] = 1
                queue.append((newx,newy))
                count+=1

    return count

ans = []
count2 = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            ans.append(bfs(i,j))
            count2+=1

ans.sort()

print(count2)
for i in ans:
    print(i, end=' ')






