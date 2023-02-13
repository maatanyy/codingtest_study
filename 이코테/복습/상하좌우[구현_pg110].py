num = int(input())
x, y = 1,1
arr = input().split()

# RLUD
dx =  [0,0,-1,1]
dy =  [1,-1,0,0]
types = ['R','L','U','D']

for i in arr:
    for j in range(len(types)):

        if i == types[j]:
            nx = x+dx[j]
            ny = y+dy[j]

        if nx<1 or ny<1 or nx>num or ny>num:
            continue

        x ,y = nx, ny

print(x,y)
