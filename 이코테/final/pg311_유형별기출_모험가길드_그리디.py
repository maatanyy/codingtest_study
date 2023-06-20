values = list(map(int,input().split()))

count = 0
values.sort()
temp = 0

for i in values:
    temp += 1
    if temp >= i:
        count += 1
        temp = 0

print(count)