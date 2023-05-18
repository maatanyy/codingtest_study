########################
# alphabets.add(graph[nx][ny])
# dfs(nx, ny, count+1)
# alphabets.remove(graph[nx][ny])
# https://sorryhyeon.tistory.com/34 참고
# dfs에서 백트랙킹
# 찾아보니 시간초과가 너무 많이 나서 정답률이 낮음, 문제가 좀 별로인감

import sys
from collections import deque


n, m = map(int, input().split())


graph = [list(input()) for _ in range(n)]

answer = 0
check = [0]*(26)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):

    global answer
    answer = max(answer, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and check[ord(graph[nx][ny])-65]==0:
            check[ord(graph[nx][ny])-65]=1
            dfs(nx, ny, count+1)            #돌리는데
            check[ord(graph[nx][ny])-65]=0 #remove 왜냐하면 최대가 아닐경우 새로운 길로 갈때 알파벳 빼줘야함


check[ord(graph[0][0])-65]=1
dfs(0, 0, 1)

print(answer)