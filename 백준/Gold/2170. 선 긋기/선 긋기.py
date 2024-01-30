import sys

num = int(input())

temp = []

for _ in range(num):
    temp.append(list(map(int,sys.stdin.readline().split())))

temp.sort()

answer = 0

start = temp[0][0]
end = temp[0][1]

for i in range(1, num):
    if temp[i][0] <= end < temp[i][1]:
        end = max(end, temp[i][1])

    elif temp[i][0] > end:
        answer += end - start
        start = temp[i][0]
        end = temp[i][1]

answer += end - start

print(answer)


