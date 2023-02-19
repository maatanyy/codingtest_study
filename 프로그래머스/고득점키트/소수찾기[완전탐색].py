# 소수판별 알고리즘 복습했음 , 이건 가능
# 문제는 permutation 쓰는 것 까지는 생각나섯 시도했는데
# 이걸 list로 담아서 꺼낼 때 join 쓰는 걸 생각을 못했다.
# join을 계속 기억해둘 필요를 느꼈음
import math
from itertools import permutations

def solution(numbers):
    answer = []
    val = [x for x in numbers]

    for i in range(1,len(val)+1):
        per = permutations(val,i)
        for number in per:
            number = int(''.join(number))
            if is_prime_number(number)==True and number not in answer:
                answer.append(number)

    count = len(answer)
    return count


def is_prime_number(x):
    if x<=1:
        return False
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임
