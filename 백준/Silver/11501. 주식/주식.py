# 앞부터 접근하여서 시간 초과남...
# 결국 풀이가 안떠올라서 찾아봤더니
# 뒤에서 부터 접근하며 최대값을 변경하는식으로 시간초과를 해결하더라
# 다음에 나오면 이런 사고가 가능하면 좋을듯

import sys
from itertools import combinations

num = int(input())

for _ in range(num):
    day = int(input())
    tempval = list(map(int, sys.stdin.readline().split()))

    ans = 0
    now = tempval[-1]
    for i in range(day - 1, -1, -1):
        if tempval[i] > now:
            now = tempval[i]
        else:
            ans += now - tempval[i]
    print(ans)


