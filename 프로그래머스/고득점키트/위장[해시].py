from itertools import combinations
# 넣는 건 잘했음
# 근데 +1해서 곱하고 -1 하는 방식은 생각을 못한듯

def solution(clothes):
    answer = 1
    save = dict()
    for i in range(len(clothes)):
        if clothes[i][1] not in save:
            save[clothes[i][1]] = 1
        else:
            save[clothes[i][1]] += 1


    temp = list(save.values())
    print(temp)
    for i in range(len(temp)):
        answer*=(temp[i]+1)

    return answer-1

clothes = [["yellow_hat", "headgear2"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))


# 첫 나의 풀이
# 조합으로 다 계산했는데 46%만 맞춤..

# from itertools import combinations
#
#
# def solution(clothes):
#     answer = 0
#     save = dict()
#     for i in range(len(clothes)):
#         if clothes[i][1] not in save:
#             save[clothes[i][1]] = 1
#         else:
#             save[clothes[i][1]] += 1
#
#     for i in save.values():
#         answer += i
#
#     temp = list(save.values())
#
#     if len(temp) == 2:
#         answer += temp[0] * temp[1]
#
#     elif len(temp) == 3:
#         combi = list(combinations(temp,2))
#         for i in range(len(combi)):
#             answer+= combi[i][0]*combi[i][1]
#         answer += temp[0]*temp[1]*temp[2]
#
#     elif len(temp) == 4:
#         combi = list(combinations(temp,2))
#         for i in range(len(combi)):
#             answer+= combi[i][0]*combi[i][1]
#
#         combi2 = list(combinations(temp,3))
#         for i in range(len(combi2)):
#             answer += combi2[i][0]*combi2[i][1]*combi2[i][2]
#
#         answer += temp[0] * temp[1] * temp[2] * temp[3]
#
#     return answer
#
# clothes = [["yellow_hat", "headgear2"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# print(solution(clothes))