import sys
from collections import deque

v, e = map(int, sys.stdin.readline().split())

graph = [ [] for i in range(v+1)]
indegree = [0] * (v+1)

for _ in range(e):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b]+=1


def to_sort():
    q = deque()
    result = []

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    for i in result:
        print(i, end =' ')

to_sort()
