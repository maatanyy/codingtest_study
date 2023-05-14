import sys
num = int(input())

# 예상등수
tempans = []

# 실제등수
ans = []

for i in range(num):
    ans.append(i+1)

for i in range(num):
    x = int(sys.stdin.readline())
    tempans.append(x)

tempans.sort()

sum = 0

for i in range(num):
    if ans[i]!=tempans[i]:
        sum += abs(ans[i]-tempans[i])

print(sum)

