from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

# def dfs(graph,v,visited):
#     visited[v]=True
#     print(v,end=' ')
#
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)
#
# dfs(graph,1, visited)

# def bfs(graph,v,visited):
#     queue = deque([v])
#     visited[v] = True
#
#     while queue:
#         x = queue.popleft()
#         print(x,end=' ')
#
#         for i in graph[x]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i]=True
#
# bfs(graph,1,visited)





















