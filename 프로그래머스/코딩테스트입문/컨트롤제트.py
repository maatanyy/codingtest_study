def solution(s):
    answer = 0
    s = s.split(' ')
    print(s)
    for i in range(len(s)):
        if s[i]=='Z':
            answer -= int(s[i-1])
        elif int(s[i])>0:
            answer += int(s[i])
        elif int(s[i])<0:
            answer += int(s[i])
    return answer
print(solution("-1 -2 -3 Z"))
