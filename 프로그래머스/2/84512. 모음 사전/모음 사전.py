from itertools import product
def solution(word):
    answer = 0
    temp = ['A','E','I','O','U']
    
    temps =[]
    
    for i in range(5):
        temps+=list(product(temp,repeat=i+1))
    
    temps.sort()
    
    for i in temps:
        answer+=1
        val = ''.join(i)
        if word == str(val):
            break
        
    
    return answer