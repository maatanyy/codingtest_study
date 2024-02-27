def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    
    temp =[]
    
    for i in data:
        if ext=='code':
            if i[0]<val_ext:
                temp.append(i)
                
        elif ext =='date':
            if i[1]<val_ext:
                temp.append(i)
            
        elif ext =='maximum':
            if i[2]<val_ext:
                temp.append(i)
            
        elif ext =='remain':
            if i[3]<val_ext:
                temp.append(i)
    
    if sort_by =='code':
        temp.sort(key = lambda x:x[0])
    elif sort_by =='date':
        temp.sort(key = lambda x:x[1])
    elif sort_by =='maximum':
        temp.sort(key = lambda x:x[2])
    elif sort_by =='remain':
        temp.sort(key = lambda x:x[3])
    
    answer = temp
    return answer