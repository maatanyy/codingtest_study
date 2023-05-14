# total을 한 줄로 적는 법을 알게 됨
import sys

x, y = map(int,sys.stdin.readline().split())
arr = []
for _ in range(x):
    x = int(input())
    arr.append(x)

start = 1
end = max(arr)

while start<=end:
    count = 0
    mid = (start+end) //2

    for i in arr:
        count += i//mid

    if count < y:
        end = mid-1

    else:
        start = mid+1

print(end)



