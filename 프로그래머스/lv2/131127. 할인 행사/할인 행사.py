def solution(want, number, discount):
    answer = 0

    length = len(discount)
    totalsum = sum(number)

    for i in range(length-totalsum+1):
        temp = discount[i:i+totalsum]

        step = 0
        for j in range(len(number)):
            if temp.count(want[j]) == number[j]:
                step+=1

        if step == len(number):
            answer+=1

    return answer