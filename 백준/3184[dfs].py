import sys
sys.setrecursionlimit(10 ** 9)

n, m = map(int,input().split())

graph = [list(input()) for _ in range(n)]

nx = [1,-1,0,0]
ny = [0,0,1,-1]

sheep = 0
wolf = 0

def dfs(x,y):
    if -1 >= x or x >= n or -1 >= y or y >= m:
        return False

    global wolf
    global sheep

    if graph[x][y] != '#':
        if graph[x][y] == 'v':
            wolf+=1
        elif graph[x][y] == 'o':
            sheep+=1
        graph[x][y] = '#'
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

        return True
    return False


sh = 0
wf = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] != '#':
            dfs(i,j)
            if sheep>wolf:
                sh +=sheep
            else:
                wf +=wolf
            sheep,wolf = 0,0

print(sh,wf)
