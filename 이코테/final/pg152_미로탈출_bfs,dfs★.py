from collections import deque
n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             newX = x + nx[i]
#             newY = y + ny[i]
#
#             if newX<0 or newY<0 or newX>=n or newY>=m:
#                 continue
#
#             if graph[newX][newY] ==0:
#                 continue
#
#             if graph[newX][newY] ==1:
#                 graph[newX][newY] = graph[x][y]+1
#                 queue.append((newX,newY))
#
#     return graph[n-1][m-1]
#
# print(bfs(0,0))

# def dfs(x,y):
#
#     if x<0 or y<0 or x>=n or y>=m:
#         return False
#
#     for i in range(4):
#         newX = x+nx[i]
#         newY = y+ny[i]
#
#         if 0<=newX<n and 0<=newY<m and graph[newX][newY]==1:
#             graph[newX][newY] = graph[x][y]+1
#
#     return False
#
# for i in range(n):
#     for j in range(m):
#         dfs(i,j)
#
# print(graph[n-1][m-1])

































