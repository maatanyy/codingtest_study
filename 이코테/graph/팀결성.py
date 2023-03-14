import sys

v, e = map(int,sys.stdin.readline().split())

parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

def find_parent(parent,x):
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())

    if a == 0:
        union_parent(parent, b,c)

    else:
        if find_parent(parent, b) == find_parent(parent, c):
            print("YES")
        else:
            print("NO")