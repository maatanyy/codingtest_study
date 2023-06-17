import sys
from collections import deque
sys.setrecursionlimit(5000)

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0]*(N+1) for i in range(N+1)]
#print(graph)

for i in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

result = 0

DFS = [0] * (N+1)
BFS = [0] * (N+1)

def dfs(v):
    DFS[v]=1
    for i in range(1,N+1):
        if not DFS[i] and graph[v][i]:
            dfs(i)


for i in range(1, N+1):
    if not DFS[i]:
        dfs(i)
        result += 1

print(result)