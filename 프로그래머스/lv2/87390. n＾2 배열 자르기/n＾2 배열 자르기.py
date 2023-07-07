# 배열 다 만들어서 하는 걸로 풀었더니 시간초과 ㅠㅠ 풀이 안떠올라서 구글링했음

def solution(n, left, right):
    answer = []

    left, right = int(left), int(right)
    for i in range(left, right+1):
        answer.append(max((i // n), (i % n)) + 1)
        
    return answer