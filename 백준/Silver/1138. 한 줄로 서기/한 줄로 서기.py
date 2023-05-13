import sys

num = int(input())     # num 명의 사람들

values = list(map(int, input().split()))

answer = [0]* (num)

for i in range(1, num+1):
    count = values[i-1]

    if i == 1:
        answer[count] = i

    else:
        val = 0

        for j in range(len(answer)):

            if val == count and answer[j]!=0:
                continue

            elif val==count and answer[j]==0:
                answer[j] = i
                break

            if answer[j]==0:
                val+=1
                continue

for ans in answer:
    print(ans,end=' ')





