n = int(input())

values = list(map(int,input().split()))

values.sort()

target = 1

for x in values:
    print(target)
    if target<x:
        break
    target+=x

print(target)