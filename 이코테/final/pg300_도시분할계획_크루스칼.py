n, m = map(int, input().split())  # n 집 m 길

graph = [ [] for _ in range(n+1) ]

edges = []

parent = [0] * (n+1)

for i in range(1,n+1):
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
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()


val = 0
result = 0
for cost,a,b in edges:
    if find_parent(parent,a)!= find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        val = cost

print(result-val)
























