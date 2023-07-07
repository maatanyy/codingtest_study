def solution(n):
    count = 0
    
    while True:
        if n==1:
            count+=1
            break
        elif n==0:
            break
        if n%2==0:
            n = n//2
        else:
            count+=1
            n = n-1
    ans = count   
    return ans