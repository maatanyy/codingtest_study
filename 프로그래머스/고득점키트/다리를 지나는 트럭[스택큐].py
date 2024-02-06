from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    temp = [0] * bridge_length
    temp = deque(temp)
    
    sumval = 0 
    
    while True:
        print(temp)
        
        if len(truck_weights) == 0:
            break

        if sumval + truck_weights[0] <= weight:   # 올릴 수 있는 경우

            a = temp.popleft()
            sumval = sumval -a + truck_weights[0]
            temp.append(truck_weights[0])
            truck_weights = truck_weights[1:]    
            answer+=1  
        
        else:   # 아닌 경우

            a = temp.popleft()
            sumval = sumval -a
            b = truck_weights[0]

            if sumval +b <=weight:
                temp.append(b)
                sumval = sumval + b
                truck_weights = truck_weights[1:]

            else:
                temp.append(0)
        
            answer+=1
    
    tv = 0
    temp = list(temp)
    
    for i in range(len(temp)):

        if temp[len(temp)-i-1] !=0:
            tv = len(temp)-i-1
            break
    
    answer +=tv+1

    return answer


print(solution(2, 10, [7,4,5,6,3,9,2,6,4,8,2,4,1]))


#    for i in truck_weights:

#        if sumval + i <= weight:
#           a = temp[0]
#            temp.popleft()
#            temp.append(i)
#            sumval = sumval - a + i
        
#        else:
#            a = temp[0]
#            temp.popleft()
#            temp.append(0)
#            sumval = sumval - a
        
#        answer+=1 
    