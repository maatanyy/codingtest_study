import sys
from itertools import combinations

num, sumval = map(int,input().split())

templist = list(map(int,input().split()))

vals = []
count = 0

for i in range(1,num+1):
    vals += list(combinations(templist,i))

for i in vals:
    if sum(i)== sumval:
        count+=1

print(count)