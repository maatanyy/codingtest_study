import sys
n = int(input())

values = list(map(int,sys.stdin.readline().split()))
values.sort()

if n%2==0:
    mid = n//2
    check = mid-1
    check2 = mid

    sum1 = 0
    sum2 = 0

    for i in values:
        sum1 += abs(values[check]-i)

    for i in values:
        sum2 += abs(values[check2]-i)

    if sum1<=sum2:
        print(values[check])
    else:
        print(values[check2])

elif n%2==1:
    mid = (n-1)//2
    print(values[mid])















