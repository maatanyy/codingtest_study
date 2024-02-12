n, m = map(int,input().split())

x, y, direction = map(int,input().split())

# direction 0 북 1 동 2 남 3 서

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

answer = 0


visited = [[False] *(m) for _ in range(n)]  #청소하면 visited 를 True로 하자,

def change():
    global direction
    direction -=1

    if direction<0:
        direction = 3



dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


while True:
    if graph[x][y] == 0 and visited[x][y] == False:
        visited[x][y] = True
        answer+=1

    count = 0
    for i in range(4):
        nexX = x+dx[i]
        newY = y+dy[i]
        if 0<=nexX < n and 0<=newY<m and visited[nexX][newY] == False and graph[nexX][newY]==0:  # 청소되지 않은 칸 
            count+=1
        
    
    if count==0:  # 청소되지 않은 칸이 없는 경우 
        newX = x-dx[direction]
        newY = y-dy[direction]
        
        if 0<=newX < n and 0 <=newY <m and graph[newX][newY] !=1:
            x = newX
            y = newY
        
        elif graph[newX][newY] == 1:
            break
    
    elif count!=0:

        for _ in range(4):
            change()

            newX = x+dx[direction]
            newY = y+dy[direction]

            if 0<=newX<n and 0<=newY<m and graph[newX][newY] == 0 and visited[newX][newY] == False:
                x = newX
                y = newY
                break

print(answer)

