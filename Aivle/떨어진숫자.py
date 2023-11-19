# 준하는 어떤 수 하나를 들고 가는 중 실수로 땅에 떨어뜨리고 말았습니다.
# 땅에 떨어진 수는 여러 개의 숫자들로 분리되었고, 준하는 이 숫자들을 황급히 주워 담기 시작했습니다.
# 준하는 주워담은 숫자 중 빠진 것이나 원래 갖고 있지  않은 것이 섞여 있지는 않는지 궁금해졌습니다.
# 준하를 위해 이를 해결해 주는 프로그램을 작성해 주세요.
import sys

temp = input()
temp2 = input()

if len(temp) != len(temp2):
    print('NO')
    sys.exit()

else:
    ans = {}

    for i in temp:
        if i not in ans:
            ans[i] = 1
        else:
            ans[i]+=1

    for i in temp2:
        if i in ans:
            ans[i]-=1
        else:
            print('NO')
            sys.exit()

    for i in ans.values():
        if i!=0:
            print('NO')
            sys.exit()

    print('YES')