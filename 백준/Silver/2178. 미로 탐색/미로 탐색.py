from collections import deque

n, m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

visited = [[False]* m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            newX = x+dx[i]
            newY = y+dy[i]
            
            if 0<=newX <n and 0<=newY <m  and visited[newX][newY]==False and graph[newX][newY]==1:
                graph[newX][newY]= graph[x][y]+1
                visited[newX][newY] = True
                queue.append((newX,newY))
                
    return graph[n-1][m-1]
        


print(bfs(0, 0))
