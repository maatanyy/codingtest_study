import sys

n = int(input())

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b


for i in range(n):
    v, e = map(int, sys.stdin.readline().split())

    parent = [0] * (v+1)
    count = 0

    for i in range(1, v+1):
        parent[i] = i

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())

        if find_parent(parent,a) != find_parent(parent,b):
            count+=1
            union_parent(parent,a,b)

    print(count)


