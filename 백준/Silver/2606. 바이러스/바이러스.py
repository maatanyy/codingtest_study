import sys

num = int(input())
count = int(input())

graph = [[] for _ in range(num+1)]
visited = [False] * (num+1)

ans = 0
def dfs(graph, visited, v):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, visited, i)
            global ans
            ans += 1

for _ in range(count):
    a, b = map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

dfs(graph,visited,1)
print(ans)




