def solution(sizes):
    temp1 = []
    temp2 = []
    
    for i in range(len(sizes)):
        a , b = sizes[i][0], sizes[i][1]
        
        if a>=b:
            temp1.append(a)
            temp2.append(b)
        else:
            temp1.append(b)
            temp2.append(a)
        
        answer = max(temp1)* max(temp2)
    return answer