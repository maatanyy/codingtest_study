def solution(answers):
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    result = []
    
    for x,y in enumerate(answers):
        if one[x%len(one)] == y:
            count[0]+=1
        if two[x%len(two)] == y:
            count[1]+=1
        if three[x%len(three)] == y:
            count[2]+=1
    
    for idx, val in enumerate(count):
        if val == max(count):
            result.append(idx+1)
    
    
    return result