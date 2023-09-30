from itertools import permutations

def make(numbers):
    number = int(''.join(numbers))
    return number

def check(numbers):

    if numbers==1 or numbers==0:
        return False
    
    if numbers ==2 or numbers==3:
        return True
    
    for i in range(2,numbers):
        if numbers%i==0:
            return False
        
    return True
                        
            
            
def solution(numbers):
    answer = 0
    temp = [i for i in numbers]
    length = len(numbers)
    
    temp2 = []
    
    for i in range(length):
        temp2 += list(permutations(temp,i+1))
    
    vals = []
    for i in temp2:
        val = make(i)
        vals.append(val)
    
    vals = list(set(vals))
    
    print(vals)
    
    for i in vals:
        if check(i) == True:
            answer+=1
    
    return answer