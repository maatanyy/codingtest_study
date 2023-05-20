def solution(s):
    answer = []
    count = 0
    zeroCount = 0

    while s!= '1':
        count+=1
        templength = len(s)
        zero = s.count('0')
        zeroCount +=zero
        oneCount = s.count('1')
        s = bin(oneCount)
        s =s[2:]

    answer.append(count)
    answer.append(zeroCount)

    return answer

s = "01110"
print(solution(s))


