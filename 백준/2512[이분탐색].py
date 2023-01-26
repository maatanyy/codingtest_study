import sys

num = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 1
end = max(budget)

while start <= end:
    mid = (start + end) // 2

    s = sum(mid if b > mid else b for b in budget)

    if s > m:
        end = mid - 1

    else:
        start = mid + 1

print(start - 1)
