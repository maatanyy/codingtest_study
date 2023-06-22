num = int(input())

graph = []

for _ in range(num):
    graph.append(list(map(int, input().split())))

dptable = []

for i in range(1, num+1):
    temp = [0] * (i)
    dptable.append(temp)

#print(dptable)

dptable[0][0] =graph[0][0]
for i in range(1, num):
    for j in range(len(graph[i])):
        if j==0:
            dptable[i][j] = dptable[i-1][j]+graph[i][j]
        elif j== len(graph[i])-1:
            dptable[i][j] = dptable[i-1][j-1]+graph[i][j]
        else:
            dptable[i][j] = max(dptable[i-1][j-1]+graph[i][j], dptable[i-1][j]+graph[i][j])

print(max(dptable[-1]))














