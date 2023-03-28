import sys
sys.setrecursionlimit(100000)

def dfs(x,y,h):

    for i in range(4):
        newx = x+nx[i]
        newy = y+ny[i]

        if 0<=newx<num and 0<=newy<num and not visited[newx][newy] and graph[newx][newy] > h:
            visited[newx][newy] = True
            dfs(newx,newy,h)

num = int(input())

graph = [list(map(int, input().split())) for _ in range(num)]
nx = [-1,1,0,0]
ny = [0,0,1,-1]

mi = -1

for k in range(max(max(graph))):
    visited = [[False]* num for _ in range(num)]
    count = 0
    for i in range(num):
        for j in range(num):
            if graph[i][j]>k and not visited[i][j]:
                count += 1
                visited[i][j] = True
                dfs(i,j,k)
    mi = max(mi,count)

print(mi)