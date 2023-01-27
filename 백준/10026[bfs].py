from collections import deque
num = int(input())

arr = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]

visited = [[0]*num for _ in range(num)]


for i in range(num):
    arr.append(list(input()))


def bfs1(x,y):
    visited[x][y]=1
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]

            if nx <0 or nx>=num or ny<0 or ny>=num:
                continue

            if visited[nx][ny]==0 and arr[nx][ny]==arr[x][y]:
                queue.append((nx,ny))
                visited[nx][ny]=1

count1=0
count2=0

for i in range(num):
    for j in range(num):
        if visited[i][j]==0:
            bfs1(i,j)
            count1+=1

visited = [[0]*num for _ in range(num)]

for i in range(num):
    for j in range(num):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(num):
    for j in range(num):
        if visited[i][j]==0:
            bfs1(i,j)
            count2+=1

print(count1, count2)

