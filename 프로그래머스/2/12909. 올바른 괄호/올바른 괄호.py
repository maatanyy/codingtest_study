def solution(s):
    answer = True
    
    stack = []
    
    for i in s:
        if i=='(':
            stack.append(i)
        else:
            if len(stack)==0:
                answer = False
                break
            temp = stack.pop()
            if temp!='(':
                answer = False
                break
    
    if len(stack)!=0:
        answer = False
    return answer