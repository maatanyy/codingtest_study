import sys

n, k = map(int,input().split())
# n 은 국가수, k는 등수를 알고 싶은 국가

board =[]
for _ in range(n):
    a,b,c,d = map(int,input().split())

    board.append([a,[b,c,d]])

board.sort(key= lambda x:(-x[1][0],-x[1][1],-x[1][2]))

findval = board[k-1][1]

count=1
for i in board:
    if i[1] == findval:
        break
    else:
        count+=1

print(count)