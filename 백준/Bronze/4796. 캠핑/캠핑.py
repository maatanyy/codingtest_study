i = 0
while True:
    i+=1
    x,y,z = map(int,input().split())

    if x==0 and y==0:
        break

    else:
        sumval = (z//y)*x
        sumval += min((z%y), x)

        print("Case " + str(i) + ": " + str(sumval))