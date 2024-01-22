def solution(input_string):
    answer = ''
    
    temp = []
    
    for i in range(len(input_string)-1):
        if input_string[i]!= input_string[i+1]:
            temp.append(input_string[i])
    

    temp.append(input_string[-1])
    
    dict = {}
    
    for i in temp:
        if i not in dict:
            dict[i] =1
        else:
            dict[i]+=1
    
    temp = []
    for k, v in dict.items():
        if v >=2:
            temp.append(k)
            
    temp.sort()
    
    for i in temp:
        answer+=i
    
    if answer=='':
        answer='N'
    return answer