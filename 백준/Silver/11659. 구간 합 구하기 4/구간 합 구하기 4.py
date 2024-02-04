import sys

n, m = map(int,sys.stdin.readline().split())

value = list(map(int,sys.stdin.readline().split()))
sumlist = [0] * n

sumlist[0] = value[0]

for i in range(n-1):

    sumlist[i+1] = sumlist[i] + value[i+1]


for _ in range(m):

    a, b = map(int,sys.stdin.readline().split())

    if a==1:
        ans = sumlist[b-1] 
    else:
        ans = sumlist[b-1] - sumlist[a-2]

    print(ans)