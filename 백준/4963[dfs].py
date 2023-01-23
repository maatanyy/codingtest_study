# 풀고 울뻔했다
# 시파......
# dfs() 인자 떄문에 고민 이빠이 했는데 4개 전달해서 해결했고
# 런타임 에러 sys.setrecursionlimit()로 해결한다고 배웠고
# 마지막으로 dfs (b,a) 때문에 진짜 너무 힘들었다 이런 인자 왜 뒤집는건지 아직도 어렵다

import sys
sys.setrecursionlimit(100000)

x, y = map(int, sys.stdin.readline().split())

answer = []

def dfs(x,y,b,a):
    if a<=-1 or a>=x or b<=-1 or b>=y:
        return False

    if array[b][a] == True:
        array[b][a] = False
        dfs(x,y,b,a+1)
        dfs(x,y,b,a-1)
        dfs(x,y,b+1,a)
        dfs(x,y,b-1,a)
        dfs(x,y,b+1,a+1)
        dfs(x,y,b-1,a+1)
        dfs(x,y,b-1,a-1)
        dfs(x,y,b+1,a-1)
        return True

    return False

while x!=0 and y!=0:
    count = 0
    array = [[False] * x for _ in range(y)]

    #기깔났다..
    for i in range(y):
        temp = input().split(' ')
        for j in range(x):
            if temp[j]=='1':
                array[i][j] = True

    for i in range(y):
        for j in range(x):
            if dfs(x,y,i,j) == True:
                count+=1


    answer.append(count)
    count=0
    x, y = map(int, sys.stdin.readline().split())

for i in range(len(answer)):
    print(answer[i])
