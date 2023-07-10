def solution(topping):
    answer = 0

    me = {}

    for i in topping:
        if i in me:
            me[i]+=1
        else:
            me[i] = 1

    you = {}

    for t in topping:

        if len(me)==len(you):
            answer+=1

        if t not in you:
            you[t]=1

        me[t]-=1

        if me[t]==0:
            del me[t]

    return answer