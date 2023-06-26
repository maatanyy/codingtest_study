import sys
from collections import deque
F, S, G, U, D = map(int, input().split())

# 총 F층 건물
# 스타트링크가 있는 곳 G
# 강호가 지금 있는 곳 S
# U는 위로 U
# D는 아래로 D

change = [U, -D]

def bfs(S):
    visited = [False] * (F + 1)
    visited[S] = 1
    q = deque()
    q.append((S, 0))

    while q:
        loc, count = q.popleft()

        if loc == G:
            return count

        for i in range(2):
            newloc = loc+change[i]
            if 1<=newloc<=F and visited[newloc]==False:
                q.append((newloc,count+1))
                visited[newloc] = True


    return "use the stairs"

print(bfs(S))













