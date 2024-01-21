import math
vals = list(map(int,(input().split(':'))))

temp = math.gcd(vals[0],vals[1])
 
valk = []

valk.append(vals[0]//temp)
valk.append(':')
valk.append(vals[1]//temp)

for i in valk:
    print(i, end='')