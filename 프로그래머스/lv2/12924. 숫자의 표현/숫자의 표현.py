def solution(n):
    answer = 0
    check = n

    for i in range(1,n+1):
        sum = 0

        for j in range(i,n+1):
            sum+=j

            if sum == check:
                answer+=1
                break

            elif check<sum:
                break

    return answer