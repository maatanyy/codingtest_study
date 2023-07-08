d = [0] * (100001)

val = int(input())

d[1] = val

if d[1]==1:
    print(1)
    exit()
i = 2

while True:

    if d[i-1]%2==0:
        d[i] = d[i-1]/2
    else:
        d[i] = d[i-1]*3+1

    if d[i]==1:
        print(i)
        break

    i+=1