import sys

sys.setrecursionlimit(100000000)
m, n, k = map(int, input().split())
# m은 세로 n은 가로

graph = [[0 for _ in range(n)] for _ in range(m)]

#print(graph)

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[j][i] = 1

#print(graph)

def dfs(x,y):

    if x<0 or y<0 or x>=m or y>=n:
        return False

    if 0<=x<m and 0<=y<n and graph[x][y]==0:
        graph[x][y] =1
        global count
        count+=1

        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True

    return False

count = 0

vals = []

for i in range(m):
    for j in range(n):
        if dfs(i,j)==True:
            vals.append(count)
            count = 0

vals.sort()
print(len(vals))
for i in vals:
    print(i, end=' ')

