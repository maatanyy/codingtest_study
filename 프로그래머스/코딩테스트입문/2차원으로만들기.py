# 2차원으로 만들기
# 원래는 이제 반복문을 num_list 길이 만큼 반복하고 n*i 이런식으로 접근을 하였으나
# 다른 풀이를 보고 for문 인자를 3개를 줘서 접근하는 방식이 더 편리하다고 깨달았다
# 규칙을 가지고 증가, 감소하는 경우 이렇게 접근하는 방식이 더 편리한 것 같다.
def solution(num_list, n):
    answer = []

    for i in range(0, len(num_list), n):
        answer += [num_list[i:i + n]]
    return answer