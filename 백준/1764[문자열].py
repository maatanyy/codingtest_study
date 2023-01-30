import sys
n, m = map(int,sys.stdin.readline().split())

arr = []
brr = []
crr = []

for i in range(n):
    arr.append(sys.stdin.readline().rstrip())

for j in range(m):
    brr.append(sys.stdin.readline().rstrip())

ans = list(set(arr)&set(brr))
ans.sort()

print(len(ans))

for i in ans:
    print(i)