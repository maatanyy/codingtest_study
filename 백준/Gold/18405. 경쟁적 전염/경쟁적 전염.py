from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

    for j in range(n):
        if graph[i][j]!=0:
            data.append((graph[i][j],0,i,j))

data.sort()  # 정렬!!

q = deque(data)

target_s, target_x, target_y = list(map(int, sys.stdin.readline().split()))

nx = [-1, 1, 0, 0]
ny = [0, 0, 1, -1]

while q:
    loc, s, x, y = q.popleft()

    if s==target_s:
        break

    for i in range(4):
        dx = x+nx[i]
        dy = y+ny[i]

        if 0<=dx<n and 0<=dy<n:
            if graph[dx][dy]==0:
                graph[dx][dy] = loc
                q.append((loc,s+1,dx,dy))

print(graph[target_x-1][target_y-1])













