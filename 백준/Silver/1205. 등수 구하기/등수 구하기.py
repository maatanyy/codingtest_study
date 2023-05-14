import sys

n, score, p = map(int, input().split())

if n==0:
    print(1)

else:
    values = list(map(int,input().split()))
    values.append(score)
    values.sort(reverse=True)
    temp = values.index(score)

    temp = temp+1  #index +1 해야함

    if temp>p:
        print(-1)
    else:
        if n == p and score == values[-1]:  # 111111111 마지막이라 더 못넣을경우
            print(-1)
        else:
            print(temp)









