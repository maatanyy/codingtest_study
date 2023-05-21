import sys

n, L = map(int, sys.stdin.readline().split())

pools = []
for _ in range(n):
    x, y = map(int,sys.stdin.readline().split())
    pools.append((x,y))

pools.sort(key=lambda x:x[0])

cur = 0
count = 0

for start, end in pools:

    if start > end:
        continue

    if start <cur:
        start = cur

    while start<end:
        start+=L
        count+=1

    cur = start

print(count)