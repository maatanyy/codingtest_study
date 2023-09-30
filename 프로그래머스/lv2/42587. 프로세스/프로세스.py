from collections import deque
def solution(priorities, location):
    answer = 0
    temp = deque()

    for idx, val in enumerate(priorities):
        temp.append([idx, val])

    while True:
        a, b = temp.popleft()
        val = 0

        for c, d in temp:
            if b < d:
                val = -1
                break
        if val == -1:
            temp.append([a, b])

        else:
            if a == location:
                return answer + 1
            elif a!=location:
                answer += 1
