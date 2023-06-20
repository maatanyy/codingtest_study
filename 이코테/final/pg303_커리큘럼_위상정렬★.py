# copy -> copy.deepcopy() 를 알아두자
# 맨날 까먹네
# 그리고 for 문 통해 list로 값 넣는 부분이랑, max쓰는 법도 봐둬야할듯!

from collections import deque
import copy
n = int(input())

graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
indegree = [0] * (n+1)

for i in range(1, n+1):
    vals = list(map(int, input().split()))
    time[i] = vals[0]
    for data in vals[1:-1]:
        indegree[i]+=1
        graph[data].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[now]+time[i], result[i])
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    for i in range(1,n+1):
        print(result[i])

topology_sort()




