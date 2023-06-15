n, m = map(int,input().split())

values = list(map(int,input().split()))

first = max(values)

while True:
    count = 0

    for i in values:
        if i-first>0:
            count +=(i-first)


    if count < m:
        first = first-1

    else:
        break

print(first)













