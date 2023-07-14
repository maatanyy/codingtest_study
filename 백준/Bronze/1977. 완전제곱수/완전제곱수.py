import math
m = int(input())
n = int(input())

temp = []

for i in range(m,n+1):

    if int(math.sqrt(i)) == math.sqrt(i):
        temp.append(i)


if len(temp)==0:
    print(-1)
else:
    print(sum(temp))
    print(min(temp))