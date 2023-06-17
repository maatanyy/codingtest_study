# 시작 시간 : 4:31

val = int(input())
# 4라치자

d = [0] * (val+1)
#  5개짜리 만듬

temp = list(map(int, input().split()))

d[0] = temp[0]
d[1] = max(temp[0], temp[1])

for i in range(2, val):
    d[i] = max(d[i-2]+temp[i], d[i-1])

print(d[val-1])

