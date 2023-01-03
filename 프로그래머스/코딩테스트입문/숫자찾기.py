# 숫자찾기
# 숫자가 안에 있는 것 까지는 쉽게 해결하였는데 이제 없을 경우 -1 처리를 어케 할지 고민하였다
# 그래서 if 문으로 먼저 있나 확인하고 있는 경우에만 구하는식으로 해결하였다!
def solution(num, k):
    answer = 0

    if str(k) not in str(num):
        answer=-1

    else:
        for x in str(num):
            answer+=1
            if x==str(k):
                break
    return answer

solution(123456,7)