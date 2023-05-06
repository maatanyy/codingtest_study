def solution(s):
    answer = -1

    temp = []
    for i in range(len(s)):
        if not temp:
            temp.append(s[i])

        else:
            if s[i] == temp[-1]:
                temp.pop()

            else:
                temp.append(s[i])

    if temp:
        return 0
    else:
        return 1


s = 'cdcd'
print(solution(s))
