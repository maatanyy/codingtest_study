from collections import deque
import sys

sys.setrecursionlimit(100000000)
arr = []

for i in range(5):
    arr.append(list(map(int, input().split())))

nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

answer = []

def dfs(x, y, letter):
    letter += str(arr[x][y])

    if len(letter) == 6:
        answer.append(letter)
        return True

    for i in range(4):
        newX = x+nx[i]
        newY = y+ny[i]

        if 0<=newX<=4 and 0<=newY<=4:
            dfs(newX, newY, letter)


for i in range(5):
    for j in range(5):
        dfs(i,j,"")

answer = set(answer)
print(len(answer))







