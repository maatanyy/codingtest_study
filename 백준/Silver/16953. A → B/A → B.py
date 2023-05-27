x, y = map(int, input().split())
count = 0

while (y != x):
    count += 1
    temp = y
    if y%10==1:
        y//=10

    elif y%2==0:
        y//=2

    if temp==y:
        print(-1)
        exit()

print(count+1)