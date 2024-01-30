import sys
num = int(input())

temp = []

for _ in range(num):
    temp.append(int(sys.stdin.readline()))

temp.sort()

ans = [i+1 for i in range(num)]

answer = 0

for i in range(len(temp)):
    answer += abs(temp[i]-ans[i])

print(answer)