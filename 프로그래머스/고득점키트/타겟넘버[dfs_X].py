from collections import deque

def solution(numbers, target):
    length = len(numbers)
    answer = 0
    queue = deque()
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])

    while queue:
        temp, idx = queue.popleft()
        idx += 1

        if idx < length:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer