# 에러 스스로해결!
# queue를 반복문 안에서 새로 만들어야지 아니면 기존 큐에 남아 있는 값에 추가하는 형태로 진행되는걸 발견
import sys
from collections import deque

# queue에 쌓여서 FIFO에 따라 인쇄


num = int(input())

for _ in range(num):
    queue = deque()
    count = 0
    a, b = map(int, sys.stdin.readline().split())

    temp = list(map(int, input().split()))

    for i in range(0, len(temp)):
        queue.append([i, temp[i]])


    while queue:
        tempval = queue[0][1]
        maxval = max(queue, key=lambda x:x[1])[1]

        if tempval != maxval:
            queue.append([queue[0][0], queue[0][1]])
            queue.popleft()

        elif tempval == maxval:
            if queue[0][0] == b:
                count+=1
                break

            else:
                count+=1
                queue.popleft()

    print(count)