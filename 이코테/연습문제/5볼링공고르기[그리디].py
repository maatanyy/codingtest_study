import sys

n, m = map(int,input().split())

data = list(map(int,input().split()))

array = [0] * 11
result = 0

for i in data:
    array[i] += 1

for k in range(1,m+1):
    n -=array[k]

    result+= array[k]* n

print(result)

