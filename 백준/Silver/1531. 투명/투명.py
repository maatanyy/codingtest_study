n, m = map(int,input().split())

graph= [ [0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x1, y1, x2, y2 = map(int,input().split())

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            graph[i][j]+=1

count = 0

for i in range(1,101):
    for j in range(1,101):
        if graph[i][j]>m:
            count+=1

print(count)