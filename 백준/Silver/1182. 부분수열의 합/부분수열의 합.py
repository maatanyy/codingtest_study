from itertools import combinations

num, target = map(int,input().split())

temp = list(map(int,input().split()))

k = []

for i in range(len(temp)):
    tms = list(combinations(temp,i+1))

    k+=tms


count = 0
for i in k:
    if sum(i) == target:
        count+=1

print(count)