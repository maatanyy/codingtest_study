import sys

a, b, c, x, y = map(int,input().split())
sum = 0

if a+b < 2*c:
    sum += a * x + b * y

else:
    temp = min(x,y) *2*c
    if x >= y:
        temp2 = min( (x-y)*a, (x-y)*2*c)
        sum += (temp + temp2)
    else:
        temp2 = min((y-x)*b, (y-x)*2*c)
        sum+=(temp+temp2)
print(sum)
