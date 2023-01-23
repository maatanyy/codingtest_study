def solution(array):
    dict = {}

    for i in array:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1

    result = sorted(dict.items(), key=lambda x: x[-1], reverse=True)  #val 기준으로 많은거 부터 적은거

    if len(result) <= 1:
        return result[0][0]
    return result[0][0] if result[0][1] != result[1][1] else -1

solution([1, 1, 2, 2,3,4,5,5,5])


####다른 사람 풀이
#### 보고 감탄했다 와
# set이 뭔지도 까먹고 있었는데 집합이고, enumerate는 튜플로 반복문 묶는 기분
# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1