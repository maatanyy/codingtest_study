# 시작 시간 : 4:20
# 종료 시간 : 4:30

d = [0] * 30001

val = int(input())

for i in range(2,val+1):

    d[i] = d[i-1]+1  # 1뺴는 경우랑 이제 나눠지는 경우랑 비교

    if i%5==0:
        d[i] = min(d[i],d[i//5]+1)

    if i%3==0:
        d[i] = min(d[i],d[i//3]+1)

    if i%2==0:
        d[i] = min(d[i],d[i//2]+1)


print(d[val])


