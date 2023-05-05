def solution(array, commands):
    answer = []
    
    for i in commands:
        a,b,c = i
        
        temparray = array[a-1:b]
        temparray.sort()
        answer.append(temparray[c-1])
    return answer