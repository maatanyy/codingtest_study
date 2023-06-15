num = int(input())

moving = ['L','R','U','D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move = input().split()

x, y = 1, 1
for step in move:

    for j in range(len(moving)):
        if step==moving[j]:
            newX = x+dx[j]
            newY = y+dy[j]

    if newX <1 or newX > num or newY <1 or newY >num:
        continue

    x = newX
    y = newY

print(x, y)