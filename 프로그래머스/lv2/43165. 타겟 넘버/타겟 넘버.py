from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append(numbers[0])
    queue.append(-numbers[0])

    for i in range(1, len(numbers)):
        temp = []
        while queue:
            val = queue.pop()
            val1 = val+numbers[i]
            val2 = val-numbers[i]
            temp.append(val1)
            temp.append(val2)

        queue = temp

    for i in queue:
        if i == target:
            answer+=1

    return answer

numbers = [4, 1, 2, 1]
target = 4

print(solution(numbers, target))