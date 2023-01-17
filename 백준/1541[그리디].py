# 잘 해결했는데 00009-00009 가 eval 로 했을 때 오류떠서 이유를 모르겠어서 다른 풀이 찾았다
# 아마 0000상수 형태라 그런 거 같다.
# 이 방식은 이제 - 기준으로 split 하는 건 나랑 똑같은데 이제 +를 묶어서 num에 넣어주고 num 배열에서 빼는 식으로 해결
# https://blog.naver.com/dltndudvldzm/222306043382 참고
temp = input()
temp2 = temp.split('-')

num = []

for i in temp2:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt+=int(j)
    num.append(cnt)

first = num[0]

for i in range(1,len(num)):
    first= first-num[i]

print(first)
