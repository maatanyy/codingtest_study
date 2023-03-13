import sys
sys.setrecursionlimit(100000000)

def union(x,y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

n, m = map(int, sys.stdin.readline().split())

parents = [i for i in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        print(i+1)
        break
    union(a,b)
else:
    print(0)