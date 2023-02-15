from itertools import combinations
def solution(number):
    temp = list(combinations(number,3))
    count = 0
    for i in range(len(temp)):
        if temp[i][0]+temp[i][1]+temp[i][2]==0:
            count+=1
    answer = count
    return answer