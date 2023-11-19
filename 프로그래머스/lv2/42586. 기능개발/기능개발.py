from collections import deque
def solution(progresses, speeds):
    answer = []
    
    for i in range(len(progresses)):
        count = 1
        while True:
            total = progresses[i]+(speeds[i]*count)
            if total>=100:
                answer.append(count)
                break
            count+=1
            
    # [5,10,1,1,20,1]
    
    answer2 = []
    i = 0
    k = 0
    count = 1
    while True:
        k+=1
        if k == len(answer):
            break
            
        if answer[i]<answer[k]:
            answer2.append(count)
            i = k
            count = 1
        else:
            count+=1
    
    answer2.append(count)            
        
    return answer2