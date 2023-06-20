# 나는 print로 사이클 발생시 출력을 하였으나
# cycle = False로 두고 발생시 True break로 나오는게 깔끔한 것 같다 (교재 풀이)!!
n, m = map(int,input().split())

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
    a, b = map(int,input().split())
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)

    elif find_parent(parent,a)==find_parent(parent,b):
        print("사이클이 발생했습니다.")













