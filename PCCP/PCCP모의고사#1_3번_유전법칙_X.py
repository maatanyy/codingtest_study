def find(pos, num):
    stack = []
    
    while pos>1:
        stack.append(num%4)
        pos-=1
        num//=4
        
    while len(stack) > 0:
        ans = stack.pop()
            
        if ans == 0:
            return 'RR'
        if ans ==3:
            return 'rr'
        
    return 'Rr'        
         
def solution(queries):
    answer = []
    
    for i in queries:
        pos, num = i[0], i[1]
        num -=1
        
        answer.append(find(pos, num))            
    
    return answer