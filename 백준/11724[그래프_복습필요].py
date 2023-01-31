# graph 에 넣는 것 까지는 잘했고 dfs도 잘 생각했는데 문제는 이게
# 평소 dfs처럼 접근했다 N*N 형태..
# 이제 그래프 형식으로 visited느낌으로 접근을 했어햐 했다
# dfs ,bfs 풀이를 참고하였는데 복습하기 좋아보여서 자주 봐야할 것 같다
# https://blog.naver.com/kuntnsrb/222979180443 참고
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


def bfs(v):
    queue =deque()
    queue.append(v)
    BFS[v]=1

    while queue:
        t = queue.popleft()

        for i in range(1,N+1):
            if not BFS[i] and graph[t][i]:
                queue.append(i)
                BFS[i]=1


for i in range(1, N+1):
    if not BFS[i]:
        bfs(i)
        result += 1








print(result)
