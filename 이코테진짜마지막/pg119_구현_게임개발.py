n ,m = map(int,input().split())
x, y, direction = map(int, input().split())

visited = [[0]* m for _ in range(n)]
visited[x][y] =1

graph = []
a
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
# 0 육지, 1 바다

def godirection():
    global direction
    direction -=1
    if direction == -1:
        direction = 3


count = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]


step_count = 0

while True:
    godirection()
    
    nx = x+dx[direction]
    ny = y+dy[direction]
    
    if visited[nx][ny] == 0 and graph[nx][ny]==0:
        visited[nx][ny] = 1
        count+=1
        x = nx
        y = ny
        step_count = 0
        continue
    
    else:
        step_count+=1
        
    if step_count == 4:
        nx = x-dx[direction]
        ny = y-dy[direction]
        
        if graph[nx][ny] == 0:
            x = nx 
            y = ny
        
        else:
            break
        
        step_count = 0

print(count)

