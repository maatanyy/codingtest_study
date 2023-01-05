# 문자열 정렬하기
# 여기서는 이제 str에서 sort가 안되니까 list 로 변환하였는데
# lower, upper 쓸 때 이제 return 을 받아야한다!! 그냥 .()만하면 적용안됨!!!
def solution(my_string):
    answer = ''
    my_string = my_string.lower()
    my_string = list(my_string)
    my_string.sort()
    answer = ''.join(my_string)
    return answer

solution('Happy')