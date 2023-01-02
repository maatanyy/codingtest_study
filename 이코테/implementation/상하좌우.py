# 상하좌우
n = int(input())

moves=['L','R','U','D']
x, y = 1, 1
changeX = [0,0,-1,1]
changeY = [-1,1,0,0]

moving = input().split()

for move in moving:
    for i in range(len(moves)):
        if move == moves[i]:
            nX = x+changeX[i]
            nY = y+changeY[i]

    if nX <1 or nX >n or nY<1 or nY>n:
        continue

    x, y = nX, nY

print(x, y)

