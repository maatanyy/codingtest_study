#풀이 조금 참고
#어렵다
from itertools import permutations

def solution(numbers):
    answer = ''

    temp = [str(x) for x in numbers]

    temp.sort(key= lambda x:x*3, reverse=True)
    answer = ''.join(temp)
    answer = str(int(answer))

    return answer