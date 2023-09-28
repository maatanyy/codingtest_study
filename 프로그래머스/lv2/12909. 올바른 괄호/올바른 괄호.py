def solution(s):
    answer = True
    temp = []
    
    for i in s:
        if i == '(':
            temp.append(i)
        elif i == ')':
            if len(temp)!=0:
                temp.pop()
            else:
                return False
        
    if len(temp)!=0:
        return False
            

    return True