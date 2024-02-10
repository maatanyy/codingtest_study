import math
def solution(progresses, speeds):
    
    temp=[]
    
    for i in range(len(progresses)):
        count =1 
        
        while True:
            if progresses[i] +speeds[i]*count >=100:
                temp.append(count)
                break
            count+=1


    
    answer = []
    
    i = 0
    k = 0
    
    count = 1
    
    while True:
        k+=1
        if k == len(temp):
            break
            
        if temp[i]<temp[k]:
            answer.append(count)
            i = k
            count = 1
        else:
            count+=1
    
    answer.append(count)  
            
    return answer