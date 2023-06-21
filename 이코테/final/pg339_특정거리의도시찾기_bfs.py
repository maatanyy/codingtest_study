from collections import deque
import sys
n, m, k, x = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

distance = [-1]*(n+1)
distance[x] =0

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

q = deque()
q.append(x)

while q:
    now = q.popleft()

    for i in graph[now]:
        if distance[i]==-1:
            distance[i] = distance[now]+1
            q.append(i)

check = False

for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check = True

if check == False:
    print("-1")