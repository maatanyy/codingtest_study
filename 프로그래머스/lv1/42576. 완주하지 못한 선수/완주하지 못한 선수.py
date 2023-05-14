def solution(participant, completion):
    # 참여한 선수 participant, 완주한 선수 completion
    answer = ''

    dic = {}

    for i in participant:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1

    for i in completion:
        dic[i]-=1

    for i in dic.items():
        a,b = i
        if b !=0:
            answer+=a

    return answer