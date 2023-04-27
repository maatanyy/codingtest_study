num = int(input())
pair = int(input())
array = [[] for _ in range(num+1)]
count = 0
visited = [False] * (num+1)

for _ in range(pair):
    x, y = map(int, input().split())

    array[x].append(y)
    array[y].append(x)

def dfs(array, v, visited):
    visited[v] = True

    for i in array[v]:
        if not visited[i]:
            dfs(array, i, visited)

dfs(array, 1, visited)

for i in visited:
    if i == True:
        count+=1

print(count-1)  #처음 시작점 빼기

