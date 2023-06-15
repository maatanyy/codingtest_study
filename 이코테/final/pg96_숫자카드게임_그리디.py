n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

for i in graph:
    i.sort()

temp = -1

for j in graph:
    if temp<j[0]:
        temp = j[0]

print(temp)