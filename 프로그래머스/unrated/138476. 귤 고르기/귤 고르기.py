def solution(k, tangerine):
    dic = {}
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    temp = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
    arr = []

    for key, value in temp.items():
        if len(arr)<k:
            for i in range(value):
                arr.append(key)
        else:
            break

    arr = set(arr)
    answer = len(arr)

    return answer