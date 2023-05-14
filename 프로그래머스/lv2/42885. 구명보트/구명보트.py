from collections import deque
def solution(people, limit):

    answer = 0
    people.sort(reverse=True)
    queue = deque(people)

    while queue:

        if len(queue)==1:
            answer+=1
            break

        val = queue.popleft()

        if val == limit:
            answer+=1

        else:
            val2 = queue.pop()

            if val+val2 >limit:
                answer+=1
                queue.append(val2)

            else:
                answer+=1

    return answer