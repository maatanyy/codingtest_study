def solution(n, lost, reserve):
    answer = 0
    temp = [1 for _ in range(n)]
    
    for i in lost:
        temp[i-1]-=1
    
    for i in reserve:
        temp[i-1]+=1
    
    for i in range(len(temp)-1):
        
        if i==0 and temp[i]==0 and temp[i+1]==2:
            temp[i] = 1
            temp[i+1] = 1
            continue
            
        elif i!=0 and temp[i]==0 and temp[i-1]==2:
            temp[i] = 1
            temp[i-1] = 1
            continue
            
        elif i!=0 and temp[i]==0 and temp[i+1]==2:
            temp[i] = 1
            temp[i+1] = 1
            continue
            
    if temp[n-2] == 0 and temp[n-1] == 2:
        temp[n-2] = 1
        temp[n-1] = 1
    
    elif temp[n-2] == 2 and temp[n-1] == 0:
        temp[n-2] = 1
        temp[n-1] = 1
    
    print(temp)
    for i in temp:
        if i!=0:
            answer+=1
    return answer