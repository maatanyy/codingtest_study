import sys
from itertools import combinations

while True:

    val = list(map(int,input().split()))

    if len(val)==1 and val[0]==0:
        break

    else:
        temp = val[1:]

        ans = list(combinations(temp,6))

        for a in ans:
            for b in a:
                print(b, end= ' ')
            print()

    print()