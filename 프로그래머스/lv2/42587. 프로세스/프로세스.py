from collections import deque

def solution(priorities, location):
    queue = deque()

    # queue에 집어 넣기
    for i in range(len(priorities)):
        if i != location:
            queue.append((priorities[i],-1))
        elif i==location:  #찾을라고 하는 것!
            queue.append((priorities[i],-2))

    answer = 0

    while queue:
        biggest, idx2 = max(queue)
        num, idx = queue.popleft()
        if num == biggest and idx ==-2:
            answer+=1
            break

        elif num==biggest and idx==-1:
            answer+=1

        elif num < biggest:
            queue.append((num, idx))

    return answer