import sys
sys.setrecursionlimit(100000000)
num = int(input())

parents = [i for i in range(num+1)]

graph = [[] for _ in range(num+1)]

visited = [False] * (num+1)

for _ in range(num-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)

def dfs(x):

    visited[x] = True

    for i in graph[x]:
        if not visited[i]:
            parents[i] = x
            dfs(i)

dfs(1)

for i in range(2,num+1):
    print(parents[i])

