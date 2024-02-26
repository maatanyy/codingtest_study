def solution(number, k):
    answer = ''
    
    stack = []
    
    for i in number:
        
        if not stack:
            stack.append(i)
            continue
        
        if k>0:
            
            while stack[-1]<i:
                stack.pop()
                k-=1
                
                if k==0 or not stack:
                    break
        
        stack.append(i)
    
    answer = ''.join(stack)
    
    if k!=0:
        answer = answer[:-k]
        
        
    return answer