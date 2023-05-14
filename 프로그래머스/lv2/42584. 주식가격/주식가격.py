def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        count = 0
        for j in range(i,len(prices)-1):
            if prices[i]<=prices[j]:
                count+=1
            else:
                answer[i] =count
                break
            answer[i] =count

    return answer