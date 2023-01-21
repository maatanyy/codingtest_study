def solution(n):
    answer = []
    if n==1:
        answer.append(1)

    for i in range(2,n+1):
        if n%i==0:
            count = 0
            for j in range(1,i+1):
                if i%j==0:
                    count+=1
            if count==2:
                answer.append(i)
                n=n//i
    return answer

print(solution(100))
