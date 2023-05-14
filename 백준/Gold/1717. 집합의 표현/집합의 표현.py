import sys
sys.setrecursionlimit(100000000)

def union(x, y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if parent[x]!=x:
        parent[x] = find(parent[x])
    return parent[x]

n, m = map(int, sys.stdin.readline().split())

parent = [i for i in range(n+1)]


for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")


