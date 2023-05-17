n, d = map(int, input().split())

graph = []

# 전체 길이
drive = [i for i in range(d+1)]

for _ in range(n):
    a,b,c = map(int, input().split())
    graph.append((a, b, c))


for i in range(0, d+1):

    for start,end,cost in graph:
        if i==start and end<d+1:
            if cost<end-start:
                drive[end] = min(drive[end], drive[start]+cost)

                k = d+1-end
                for t in range(1,k):
                    drive[end+t] = min(drive[end+t],drive[end]+t)

print(drive[d])