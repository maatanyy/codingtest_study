def solution(participant, completion):
    
    dict = {}
    answer = ''
    
    for i in participant:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1

    for i in completion:
        if i in dict:
            dict[i] -= 1
    
    for k,v in dict.items():
        if v ==1:
            answer+=k
    
    
    return answer