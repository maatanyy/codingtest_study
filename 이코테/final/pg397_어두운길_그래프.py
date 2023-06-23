n, m = map(int, input().split())

parent = [0]* (n+1)

for i in range(1, n+1):
    parent[i] = i
print(parent)

def find_parent(parent,x):
    if parent[x]!=x:
        return find_parent(parent,parent[x])

    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a

    else:
        parent[a] = b

arr = []


for _ in range(m):
    x, y, pay = map(int, input().split())
    arr.append((pay, x, y))

arr.sort()
totalcost = 0
cost = 0

for ar in arr:
    pay,x,y = ar
    totalcost+=pay

    if find_parent(parent,x) != find_parent(parent,y):
        union_parent(parent,x,y)
        cost+=pay

print(totalcost-cost)

























