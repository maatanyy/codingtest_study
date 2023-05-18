import sys
from collections import deque

n, m, k, x = map(int,sys.stdin.readline().split())

# n: 도시, m:도로, k:거리정보, x:출발도시

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)


distance = [-1] *(n+1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()

    for nextloc in graph[now]:

        if distance[nextloc]==-1:
            distance[nextloc] = distance[now]+1
            q.append(nextloc)

check = False

for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True

if check == False:
    print(-1)