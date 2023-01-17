# 쉽게 해결 다만 ,replace 쓸 시 다 바뀐다는 걸 까먹고 있었다
x, y = map(str,input().split())
min=0
max=0
if '5' in x:
    x = x.replace('5','6')

if '5' in y:
    y = y.replace('5','6')

max = int(x) + int(y)

if '6' in x:
    x = x.replace('6','5')

if '6' in y:
    y = y.replace('6','5')

min = int(x) + int(y)

print(min, max)