def solution(s):
    answer = ''
    temp = list(map(int, s.split()))
    maxval = max(temp)
    minval = min(temp)
    answer = answer + str(minval)+ ' ' +str(maxval)
    return answer

s = "-1 -1"

print(solution(s))