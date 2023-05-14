import math
a, b = map(int,input().split())

c, d = map(int,input().split())

temp1 = b * d
temp2 = a*d + b*c

temp3 = math.gcd(temp1,temp2)

if type(temp3) == int:
    print(temp2//temp3, temp1//temp3)

else:
    print(temp2, temp1)