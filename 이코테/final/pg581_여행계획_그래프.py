# 잘푼듯 답지랑 거의 일치
import sys
INF = int(1e9)

n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

#print(graph)

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

parent = [i for i in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            union_parent(parent,i,j)

steps = list(map(int,input().split()))

check = True
for i in range(0,len(steps)-1):
    if find_parent(parent,steps[i]) == find_parent(parent,steps[i+1]):
        pass
    else:
        check = False
        print("NO")

if check==True:
    print("YES")





steps = list(map(int,input().split()))

