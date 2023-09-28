def find_parents(parent,x):
    if parent[x] == x:
        return x
    return find_parents(parent,parent[x])

def union_parents(parent,a,b):
    a = find_parents(parent,a)
    b = find_parents(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n)]
    count = 0
    
    for i in costs:
        if find_parents(parent,i[0]) != find_parents(parent,i[1]):
            union_parents(parent,i[0],i[1])
            answer+=i[2]
            count+=1
        
        if count == n-1:
            break
        
    return answer