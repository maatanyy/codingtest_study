import sys
from itertools import combinations

n, m = map(int,input().split())

card = list(map(int,sys.stdin.readline().split()))

temp = list(combinations(card, 3))

tempans =[]
for i in temp:
    val = sum(i)
    tempans.append(val)

tempans.sort()
temp = 0

for i in tempans:
    if i <=m:
        temp = i
        continue
    else:
        break

print(temp)






