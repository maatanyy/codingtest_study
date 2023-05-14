import sys
from collections import deque

def solution(maps):
    answer = 0

    n = len(maps)  # x len
    m = len(maps[0])  # y len

    queue = deque()
    queue.append((0,0))

    nx = [-1, 1, 0, 0]
    ny = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            newX = x+nx[i]
            newY = y+ny[i]

            if newX <0 or newX >= n or newY <0 or newY>=m:
                continue

            if maps[newX][newY]==0:
                continue

            if maps[newX][newY]==1:
                maps[newX][newY] = maps[x][y]+1
                queue.append((newX,newY))
        
    
    if maps[n-1][m-1] == 1:
        return -1

    return maps[n-1][m-1]