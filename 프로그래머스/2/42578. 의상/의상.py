def solution(clothes):
    dic = { v: [] for _,v in clothes}
    
    for i in clothes:
        dic[i[1]].append(i[0])
    
    answer = 1
    

    for k,v in dic.items():
        answer *= (len(v)+1)

        
    return answer-1