def solution(s):
    dic = {}
    answer= ''
    for letter in s:
        dic[letter] =0

    for letter in s:
        dic[letter] +=1

    for k,v in dic.items():
        if v==1:
            answer+=k

    answer2 = sorted(answer)

    answer = ''.join(answer2)

    return print(answer)

solution("abdc")