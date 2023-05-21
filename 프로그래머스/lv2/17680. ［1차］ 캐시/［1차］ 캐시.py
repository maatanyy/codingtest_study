from collections import deque
def solution(cacheSize, cities):
    answer = 0

    cities = [i.upper() for i in cities]

    queue = deque()

    if cacheSize==0:
        return len(cities) * 5

    for i in cities:
        if i not in queue and len(queue)<cacheSize:   # 없고 길이보다 작을 경우
            queue.append(i)
            answer+=5

        elif i not in queue and len(queue)==cacheSize:  # 없고 큐가 가득 차있는 경우
            queue.popleft()
            queue.append(i)
            answer+=5

        elif i in queue and len(queue)<cacheSize:     # 있고 길이보다 작을 경우
            queue.remove(i)
            queue.append(i)
            answer+=1

        elif i in queue and len(queue)==cacheSize:     # 있고 큐가 가득 차있는 경우
            queue.remove(i)
            queue.append(i)
            answer += 1

    return answer