# 중복된 문자 제거
# 항상 반복문을통해 비교하는 방식으로 접근하였는데 다른 풀이는 없을까 찾아보다가
# 새로운 걸 추가하는 방식을 발견하여 도움 받아 해결함

def solution(my_string):
    answer=''
    for i in my_string:
        if not i in answer:
            answer+=i
    return answer

solution('people')