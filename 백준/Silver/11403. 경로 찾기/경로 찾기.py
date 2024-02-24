num = int(input())
INF = int(1e9)

graph = [[INF]* (num) for _ in range(num)]

temp = []

for _ in range(num):
    temp.append(list(map(int,input().split())))

for i in range(num):
    for k in range(num):
        if temp[i][k]==1:
            graph[i][k] =1



for k in range(num):
    for a in range(num):
        for b in range(num):
            graph[a][b] = min(graph[a][k]+graph[k][b],graph[a][b])


for i in range(num):
    for t in range(num):
        if graph[i][t] != INF:
            graph[i][t] = 1
        else:
            graph[i][t] = 0

for i in graph:
    
    for t in range(len(i)):
        print(i[t], end=' ')
    
    print()