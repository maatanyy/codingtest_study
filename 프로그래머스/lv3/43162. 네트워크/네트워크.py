from collections import defaultdict
def find_parent(parent, x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a

    else:
        parent[a] = b

def solution(n, computers):
    length = len(computers[0])

    parent = [i for i in range(length)]

    for j in range(n):
        for k in range(n):
            if computers[j][k]==1 and j!=k:
                union_parent(parent,j,k)

    di = defaultdict(int)
    for i in parent:
        di[find_parent(parent, i)] += 1

    return len(di.items())