# 해결하다 시간 오류 떠서 딕셔너리로 푸는 풀이를 발견했는데
# 보고 지렸다...
# https://blog.naver.com/koreanraichu/222887879640 참고하였다..

import sys
x = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array2 = []

array2 = set(array)
array2 = sorted(list(array2))

#print(array2)
rank_dic = {array2[i]:i for i in range(len(array2))}
# 이 부분 지린다. 기억하자 딕셔러니로 만드는데 이제 키:value 쌍으로
# list comprehension 써서 이제
# [-10, -9, 2, 4] 를
# {-10: 0, -9: 1, 2: 2, 4: 3} 형태로 만듬

for i in array:
    print(rank_dic[i],end=" ")


