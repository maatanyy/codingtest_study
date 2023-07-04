from itertools import combinations
n, m = map(int,input().split())

graph = []

temp = 0
for _ in range(n):
    values = list(map(int,input().split()))
    temp += values.count(2)
    graph.append(values)

home = []
res = []

for i in range(n):
    for j in range(n):

        if graph[i][j]==1:
            home.append((i,j))
        elif graph[i][j]==2:
            res.append((i,j))

candidates = list(combinations(res,m))

def get_min(candidate):
    result = 0

    for x,y in home:
        temp = int(1e9)

        for nx,ny in candidate:
            temp = min(temp,abs(x-nx) +abs(y-ny))

        result +=temp

    return result

result = int(1e9)
for a in candidates:
    result = min(result,get_min(a))

print(result)













