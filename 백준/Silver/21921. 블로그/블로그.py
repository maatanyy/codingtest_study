import sys

n, x = map(int, sys.stdin.readline().split())
#

arr = list(map(int, sys.stdin.readline().split()))

value = sum(arr[:x])
biggest= value
count = 1

for i in range(x,n):
    value+=arr[i]
    value-=arr[i-x]

    if value>biggest:
        biggest = value
        count = 1

    elif value==biggest:
        count+=1


if value==0:
    print('SAD')
else:
    print(biggest)
    print(count)