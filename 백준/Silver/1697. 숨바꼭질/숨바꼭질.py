from collections import deque

x, y = map(int, input().split())

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()

        if x==y:
            print(distance[x])
            break

        for i in (x+1,x-1,x*2):
            if 0<=i<=MAX and not distance[i]:
                distance[i] = distance[x]+1
                q.append(i)

MAX = 10**5
distance = [0] * (MAX+1)

bfs(x)











