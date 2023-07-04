n = int(input())

k = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int,input().split())
    graph[a][b] = 1


dx = [ 0, 1, 0, -1]
dy = [ 1, 0, -1, 0]

l = int(input())

steps = []

for _ in range(l):
    values = input().split()
    steps.append((int(values[0]),values[1]))


direction = 0

def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


def simulate():

    x, y = 1, 1
    time = 0
    graph[x][y] = 2
    q = [(x,y)]

    while True:
        nx = x+dx[direction]
        ny = y+dy[direction]

        if 1<=nx<=n and 1<=ny<=n and graph[nx][ny]!=2:

            if graph[nx][ny]==1:
                graph[nx][ny] = 2
                q.append((nx,ny))

            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx,ny))
                pasx, pasy = q.pop(0)
                graph[pasx][pasy] = 0

        else:
            time+=1
            break

        x , y = nx, ny
        time+=1

        for i in steps:
            if i[0]==time:
                if i[1]=='D':
                    turn_right()
                else:
                    turn_left()

    return time

print(simulate())
























