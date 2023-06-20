n, m = map(int,input().split())

parent = [0] *(n+1)

for i in range(n+1):
    parent[i] = i

def find_parent(parent,a):
    if parent[a]!=a:
        return find_parent(parent,parent[a])
    return parent[a]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    a,b,c = map(int,input().split())

    if a ==0:
        union_parent(parent,b,c)

    elif a==1:
        if find_parent(parent,b)==find_parent(parent,c):
            print("YES")
        else:
            print("NO")











