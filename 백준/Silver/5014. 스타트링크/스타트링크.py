# 총 F층, 스타트 링크 G층, 강호가 있는 곳 S층
# U버튼 은 위로 U, D 버튼은 아래로 D층
# 갈 수 없다면 "use the stairs"

import sys
sys.setrecursionlimit(100000000)
from collections import deque

F, S, G, U, D = map(int, input().split())

changes = [U, -D]

def bfs(S):
    visited = [False] * (F+1)
    visited[S] = 1
    q = deque()
    q.append((S, 0))

    while q:
        location, count = q.popleft()

        if location == G:
            return count

        for i in range(2):
            newlocation = location+changes[i]

            if 1<=newlocation<=F and visited[newlocation]==False:
                q.append((newlocation,count+1))
                visited[newlocation] = True

    return "use the stairs"


print(bfs(S))