# 3분컷했다..
def solution(common):
    answer = 0
    if common[2]-common[1] == common[1]-common[0]:
        answer = common[-1]+common[2]-common[1]
    elif common[2]//common[1] == common[1] //common[0]:
        answer = common[-1] * (common[2]//common[1])
    return answer