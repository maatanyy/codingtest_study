from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)


    while True:
        if len(people)==1:
            answer+=1
            break

        if len(people)==0:
            break

        if people[0]+people[-1] > limit:
            answer+=1
            people.pop()
            continue
        
        elif people[0] + people[-1] <=limit:
            answer+=1
            people.pop()
            people.popleft()
            
                
    return answer
