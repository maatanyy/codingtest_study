import sys
from collections import deque

n, d, k, c = map(int, input().split())
# 접시의 수 n, 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c

values = []

for _ in range(n):
    a = int(sys.stdin.readline())
    values.append(a)

ans = 0

for i in range(n):

    if i+k>=n:
        t = i+k-n
        temp = values[i:]+values[:t]

    else:
        temp = values[i:i+k]

    temp2 = set(temp)

    if c not in temp2 and len(temp2) == k:
        ans = k+1
        break

    elif c not in temp2 and len(temp2) != k:
        ans = max(ans,len(temp2)+1)

    elif c in temp2 and len(temp2)!=k:
        ans = max(ans,len(temp2))

    elif c in temp2 and len(temp2)==k:
        ans = max(ans,len(temp2))

print(ans)

