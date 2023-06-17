import sys
sys.setrecursionlimit(1000000000)
num = int(input())

for _ in range(num):
    x, y, z = map(int,input().split())

    graph = [[0]*(x) for _ in range(y)]

    for i in range(z):
        a, b = map(int,input().split())
        graph[b][a] = 1


    def dfs(w,k):
        if w<0 or w>=y or k<0 or k>=x:
            return False

        if 0<=w<y and 0<=k<x and graph[w][k]==1:
            graph[w][k]=0
            dfs(w+1,k)
            dfs(w-1,k)
            dfs(w,k+1)
            dfs(w,k-1)
            return True

        return False

    count = 0
    for i in range(y):
        for j in range(x):
            if dfs(i,j)==True:
                count+=1

    print(count)