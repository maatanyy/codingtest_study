x, y, z = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
first = arr[-1]
second = arr[-2]

sum = 0
for i in range(y):
    if (i+1)% z ==0:
        sum+=second
    else:
        sum+=first

print(sum)


