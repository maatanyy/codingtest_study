def solution(sizes):
    
    for i in sizes:
        i.sort()
        
    print(sizes)
    temp1 = -1
    temp2 = -1
    
    for a,b in sizes:

        if temp1<a:
            temp1 = a
        if temp2<b:
            temp2 = b
    
    print(temp1, temp2)
    answer = temp1*temp2
    
    return answer