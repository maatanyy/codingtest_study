n, m = map(int,input().split())
# 세로 n 가로 m

graph = []

for i in range(n):
    graph.append(list(map(int,input())))


def dfs(x,y):
    
    if 0<=x<n and 0<=y<m and graph[x][y]==0:
        graph[x][y]=1
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y)
        dfs(x+1,y)
        return True
    
    return False
            
    
count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) ==True:
            count+=1
            
print(count)