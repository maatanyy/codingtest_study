# 순열로 접근 성공 , 문제는 중복 순열을 라이브러리가 있을 것 같긴한데 뭔지 몰라서 검색해봤다가 product라고 알게 됨
# 쓰는 법은 combintations permutions와 비슷해서 바로 풀 수 있었음
# repeat = 숫자만 인지하면 될듯 그리고 중복조합은 combinations_with_replacement 라는 것도 알게 되었다!
import itertools
from itertools import product


def solution(word):
    val = ['A', 'E', 'I', 'O', 'U']
    temp = []

    for i in range(5):
        ans = list(itertools.product(val, repeat=i + 1))

        for j in ans:
            temp.append(''.join(j))

    temp.sort()

    count = 1

    return temp.index(word)+1



print(solution("AAAE"))