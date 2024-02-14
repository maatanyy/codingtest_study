import sys
import math
n = int(input())

members = list(map(int,sys.stdin.readline().split()))
b, c = map(int,input().split())

ans = 0

for i in range(len(members)):
    members[i] -= b
    ans+=1


for i in members:

    if i > 0:
        temp = math.ceil(i/c)
        ans+=temp



print(ans)
