from collections import deque

n, m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[False]*(m) for _ in range(n)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y):

    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:

        x,y = queue.popleft()

        for i in range(4):
            newx = x+dx[i]
            newy = y+dy[i]

            if 0<=newx < n and 0<=newy <m and visited[newx][newy] == False and graph[newx][newy]==1:

                graph[newx][newy] = graph[x][y]+1
                visited[newx][newy] = True

                queue.append((newx,newy))




bfs(0,0)

print(graph[n-1][m-1])