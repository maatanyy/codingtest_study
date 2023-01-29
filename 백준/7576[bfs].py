# queue 는 잘 짜는데 아직 count를 어디서 해야하나에 대한 공부가 부족하다.
# 이 부분 때문에 다른 풀이를 참고하였고
# 무엇보다 아직도 n,m 가로 ㅅ로 길이 반복문이 너무 할 떄마다 이해가 안된다
# 이거 때매 매우 짜증난다

from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
## 가로 6 세로 4

arr = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(m):
    arr.append(list(map(int,input().split())))

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx <m and 0 <=ny < n:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y]+1
                    queue.append((nx,ny))

queue=deque()

for i in range(m):
    for j in range(n):
        if arr[i][j]==1:
            queue.append((i,j))

bfs()

maxValue = 1
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            print(-1)
            sys.exit()
        maxValue = max(maxValue, arr[i][j])

if maxValue == 1:
    print(0)
else:
    print(maxValue - 1)
