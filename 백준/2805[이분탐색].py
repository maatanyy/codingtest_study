# total을 한 줄로 적는 법을 알게 됨
import sys

x, y = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(arr)
answer = 0

while start<=end:
    mid = (start+end) //2
    total = sum((b-mid) if b>mid else 0 for b in arr)

    if total >=y:
        start = mid+1
    else:
        end = mid-1

print(end)

